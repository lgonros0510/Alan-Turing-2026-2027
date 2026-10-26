from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Article


def home(request):
	articles = Article.objects.filter(
		is_published=True,
		published_at__lte=timezone.now(),
	).order_by("-published_at", "-pk")
	return render(request, "blog/home.html", {"articles": articles})


def article_detail(request, slug):
	try:
		article = get_object_or_404(
			Article.objects.filter(is_published=True, published_at__lte=timezone.now()),
			slug=slug,
		)
	except Http404:
		return render(request, "blog/404.html", status=404)
	return render(request, "blog/article_detail.html", {"article": article})
