from django.utils.text import slugify
from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
	titulo = serializers.CharField(source="title", max_length=200)
	cuerpo = serializers.CharField(source="content")
	estado = serializers.SerializerMethodField()

	class Meta:
		model = Article
		fields = ("id", "titulo", "cuerpo", "estado")
		read_only_fields = ("id", "estado")

	def get_estado(self, article):
		return "publicado" if article.is_published else "borrador"

	def create(self, validated_data):
		title = validated_data["title"]
		slug_field = Article._meta.get_field("slug")
		max_length = slug_field.max_length
		base_slug = slugify(title)[:max_length].rstrip("-") or "articulo"
		slug = base_slug
		suffix = 2

		while Article.objects.filter(slug=slug).exists():
			suffix_text = f"-{suffix}"
			slug = (
				f"{base_slug[:max_length - len(suffix_text)].rstrip('-')}"
				f"{suffix_text}"
			)
			suffix += 1

		return Article.objects.create(
			title=title,
			slug=slug,
			content=validated_data["content"],
			author="Equipo editorial",
			is_published=False,
		)
