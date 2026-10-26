from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Article


class ArticlePageTests(TestCase):
	def setUp(self):
		Article.objects.all().delete()
		self.now = timezone.now()

	def create_article(self, **overrides):
		values = {
			"title": "Robots que exploran",
			"slug": "robots-que-exploran",
			"excerpt": "Cómo se orientan los robots móviles.",
			"content": "## Percepción\n\nEl robot combina sus sensores.",
			"author": "Lucía Robles",
			"published_at": self.now,
			"is_published": True,
		}
		values.update(overrides)
		return Article.objects.create(**values)

	def test_home_lists_published_articles_newest_first_and_hides_drafts(self):
		older = self.create_article(
			title="Sensores en el taller",
			slug="sensores-en-el-taller",
			published_at=self.now - timedelta(days=2),
		)
		newest = self.create_article(
			title="Robots en movimiento",
			slug="robots-en-movimiento",
			published_at=self.now - timedelta(days=1),
		)
		self.create_article(
			title="Borrador privado",
			slug="borrador-privado",
			is_published=False,
		)

		response = self.client.get(reverse("home"))

		self.assertEqual(response.status_code, 200)
		self.assertEqual(list(response.context["articles"]), [newest, older])
		self.assertContains(response, newest.title)
		self.assertContains(response, newest.published_at.strftime("%Y"))
		self.assertContains(response, newest.excerpt)
		self.assertContains(response, newest.get_absolute_url())
		self.assertNotContains(response, "Borrador privado")

	def test_home_shows_message_when_there_are_no_published_articles(self):
		self.create_article(is_published=False)

		response = self.client.get(reverse("home"))

		self.assertContains(response, "Todavía no hay artículos publicados.")

	def test_article_page_renders_metadata_and_markdown_structure(self):
		article = self.create_article()

		response = self.client.get(article.get_absolute_url())

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, article.title)
		self.assertContains(response, article.author)
		self.assertContains(response, article.published_at.strftime("%Y"))
		self.assertContains(response, "<h2>Percepción</h2>")
		self.assertContains(response, "<p>El robot combina sus sensores.</p>")
		self.assertContains(response, reverse("home"))

	def test_missing_and_unpublished_articles_return_404(self):
		draft = self.create_article(is_published=False)

		missing_response = self.client.get("/articulos/no-existe/")
		draft_response = self.client.get(draft.get_absolute_url())

		self.assertEqual(missing_response.status_code, 404)
		self.assertContains(missing_response, "Esta página no se encuentra.", status_code=404)
		self.assertEqual(draft_response.status_code, 404)

	def test_future_articles_are_not_public(self):
		article = self.create_article(published_at=self.now + timedelta(days=1))

		home_response = self.client.get(reverse("home"))
		detail_response = self.client.get(article.get_absolute_url())

		self.assertNotContains(home_response, article.title)
		self.assertEqual(detail_response.status_code, 404)


class ArticlePublicationAdminTests(TestCase):
	def setUp(self):
		user_model = get_user_model()
		self.editor = user_model.objects.create_superuser(
			username="editor",
			email="editor@example.com",
			password="test-password",
		)
		self.client.force_login(self.editor)
		self.article = Article.objects.create(
			title="Artículo de prueba",
			slug="articulo-de-prueba",
			content="Contenido de prueba.",
			author="Equipo editorial",
		)

	def test_publication_field_is_labeled_and_defaults_to_false(self):
		publication_field = Article._meta.get_field("is_published")

		self.assertEqual(publication_field.verbose_name, "Publicado")
		self.assertFalse(publication_field.default)
		self.assertFalse(self.article.is_published)

	def test_admin_form_exposes_publication_checkbox(self):
		response = self.client.get(
			reverse("admin:blog_article_change", args=[self.article.pk])
		)

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'name="is_published"')
		self.assertContains(response, "Publicado")

	def test_admin_list_can_edit_publication_state(self):
		response = self.client.get(reverse("admin:blog_article_changelist"))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Publicado")
		self.assertContains(response, 'name="form-0-is_published"')
