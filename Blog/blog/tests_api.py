from datetime import timedelta

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Article


class ArticleAPITests(APITestCase):
	def setUp(self):
		Article.objects.all().delete()
		self.now = timezone.now()
		self.admin = get_user_model().objects.create_superuser(
			username="api-admin",
			email="api-admin@example.com",
			password="test-password",
		)
		self.admin_token = Token.objects.create(user=self.admin)
		self.list_url = reverse("api_article_list")

	def create_article(self, **overrides):
		values = {
			"title": "Robots que exploran",
			"slug": "robots-que-exploran",
			"content": "El robot combina sus sensores.",
			"author": "Lucía Robles",
			"published_at": self.now,
			"is_published": True,
		}
		values.update(overrides)
		return Article.objects.create(**values)

	def test_public_list_includes_only_available_published_articles(self):
		published = self.create_article()
		self.create_article(
			title="Borrador privado",
			slug="borrador-privado",
			is_published=False,
		)
		self.create_article(
			title="Publicación futura",
			slug="publicacion-futura",
			published_at=self.now + timedelta(days=1),
		)

		response = self.client.get(self.list_url)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(
			response.data,
			[
				{
					"id": published.pk,
					"titulo": published.title,
					"cuerpo": published.content,
					"estado": "publicado",
				}
			],
		)

	def test_public_detail_returns_published_article(self):
		article = self.create_article()

		response = self.client.get(
			reverse("api_article_detail", args=[article.pk])
		)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data["id"], article.pk)
		self.assertEqual(response.data["titulo"], article.title)
		self.assertEqual(response.data["cuerpo"], article.content)
		self.assertEqual(response.data["estado"], "publicado")

	def test_detail_hides_drafts_future_and_missing_articles(self):
		draft = self.create_article(
			title="Borrador privado",
			slug="borrador-privado",
			is_published=False,
		)
		future = self.create_article(
			title="Publicación futura",
			slug="publicacion-futura",
			published_at=self.now + timedelta(days=1),
		)

		for article_id in (draft.pk, future.pk, 999999):
			with self.subTest(article_id=article_id):
				response = self.client.get(
					reverse("api_article_detail", args=[article_id])
				)
				self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_post_without_token_is_rejected(self):
		before = Article.objects.count()

		response = self.client.post(
			self.list_url,
			{"titulo": "Borrador nuevo", "cuerpo": "Texto del borrador."},
			format="json",
		)

		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
		self.assertEqual(Article.objects.count(), before)

	def test_post_with_non_admin_token_is_rejected(self):
		user = get_user_model().objects.create_user(
			username="api-reader",
			email="api-reader@example.com",
			password="test-password",
		)
		token = Token.objects.create(user=user)
		self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
		before = Article.objects.count()

		response = self.client.post(
			self.list_url,
			{"titulo": "Borrador nuevo", "cuerpo": "Texto del borrador."},
			format="json",
		)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
		self.assertEqual(Article.objects.count(), before)

	def test_admin_token_creates_unpublished_article_with_model_defaults(self):
		self.client.credentials(
			HTTP_AUTHORIZATION=f"Token {self.admin_token.key}"
		)

		response = self.client.post(
			self.list_url,
			{
				"titulo": "Borrador nuevo",
				"cuerpo": "Texto del borrador.",
				"estado": "publicado",
				"is_published": True,
			},
			format="json",
		)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(
			set(response.data),
			{"id", "titulo", "cuerpo", "estado"},
		)
		self.assertEqual(response.data["titulo"], "Borrador nuevo")
		self.assertEqual(response.data["cuerpo"], "Texto del borrador.")
		self.assertEqual(response.data["estado"], "borrador")

		article = Article.objects.get(pk=response.data["id"])
		self.assertFalse(article.is_published)
		self.assertEqual(article.slug, "borrador-nuevo")
		self.assertEqual(article.author, "Equipo editorial")
		self.assertEqual(article.excerpt, "")
		self.assertIsNotNone(article.published_at)

	def test_post_generates_a_unique_slug_when_title_already_exists(self):
		self.create_article(
			title="Borrador nuevo",
			slug="borrador-nuevo",
		)
		self.client.credentials(
			HTTP_AUTHORIZATION=f"Token {self.admin_token.key}"
		)

		response = self.client.post(
			self.list_url,
			{"titulo": "Borrador nuevo", "cuerpo": "Otro texto."},
			format="json",
		)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(
			Article.objects.get(pk=response.data["id"]).slug,
			"borrador-nuevo-2",
		)

	def test_post_rejects_missing_blank_and_oversized_fields(self):
		self.client.credentials(
			HTTP_AUTHORIZATION=f"Token {self.admin_token.key}"
		)
		invalid_payloads = (
			{"titulo": "Falta el cuerpo"},
			{"cuerpo": "Falta el título"},
			{"titulo": "", "cuerpo": "Cuerpo"},
			{"titulo": "Título", "cuerpo": ""},
			{"titulo": "T" * 201, "cuerpo": "Cuerpo"},
		)
		before = Article.objects.count()

		for payload in invalid_payloads:
			with self.subTest(payload=payload):
				response = self.client.post(
					self.list_url,
					payload,
					format="json",
				)
				self.assertEqual(
					response.status_code,
					status.HTTP_400_BAD_REQUEST,
				)

		self.assertEqual(Article.objects.count(), before)
