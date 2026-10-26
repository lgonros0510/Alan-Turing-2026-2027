from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ("title", "author", "published_at", "is_published")
	list_editable = ("is_published",)
	list_filter = ("is_published", "published_at")
	search_fields = ("title", "excerpt", "content", "author")
	prepopulated_fields = {"slug": ("title",)}
