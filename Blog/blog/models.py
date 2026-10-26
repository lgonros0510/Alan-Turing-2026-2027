import bleach
import markdown
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe
from django.utils.text import Truncator


class Article(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	excerpt = models.CharField(max_length=280, blank=True)
	content = models.TextField(
		help_text="Escribe el contenido en Markdown. Se admiten párrafos y subtítulos."
	)
	author = models.CharField(max_length=120)
	published_at = models.DateTimeField(default=timezone.now)
	is_published = models.BooleanField(
		"Publicado",
		default=False,
		help_text="Indica si el artículo se muestra en el sitio público.",
	)

	class Meta:
		ordering = ["-published_at", "-pk"]
		verbose_name = "artículo"
		verbose_name_plural = "artículos"

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("article_detail", kwargs={"slug": self.slug})

	@property
	def summary(self):
		if self.excerpt:
			return self.excerpt
		rendered = markdown.markdown(self.content, extensions=["extra"])
		return Truncator(strip_tags(rendered)).chars(220)

	@property
	def rendered_content(self):
		rendered = markdown.markdown(self.content, extensions=["extra", "sane_lists"])
		safe_html = bleach.clean(
			rendered,
			tags={
				"a", "blockquote", "br", "code", "em", "h2", "h3", "hr", "li",
				"ol", "p", "pre", "strong", "table", "tbody", "td", "th", "thead",
				"tr", "ul",
			},
			attributes={"a": ["href", "title"]},
			protocols={"http", "https", "mailto"},
			strip=True,
		)
		return mark_safe(safe_html)
