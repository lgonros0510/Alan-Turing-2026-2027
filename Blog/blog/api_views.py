from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAdminUser

from .api_serializers import ArticleSerializer
from .models import Article


class ArticleListCreateAPIView(ListCreateAPIView):
	serializer_class = ArticleSerializer
	authentication_classes = (TokenAuthentication,)

	def get_queryset(self):
		return Article.objects.filter(
			is_published=True,
			published_at__lte=timezone.now(),
		).order_by("-published_at", "-pk")

	def get_permissions(self):
		if self.request.method == "POST":
			return [IsAdminUser()]
		return [AllowAny()]


class ArticleDetailAPIView(RetrieveAPIView):
	serializer_class = ArticleSerializer
	authentication_classes = (TokenAuthentication,)

	def get_queryset(self):
		return Article.objects.filter(
			is_published=True,
			published_at__lte=timezone.now(),
		)

	def get_permissions(self):
		return [AllowAny()]
