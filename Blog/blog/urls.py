from django.urls import path

from . import api_views
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("articulos/<slug:slug>/", views.article_detail, name="article_detail"),
    path("api/articulos/", api_views.ArticleListCreateAPIView.as_view(), name="api_article_list"),
    path(
        "api/articulos/<int:pk>/",
        api_views.ArticleDetailAPIView.as_view(),
        name="api_article_detail",
    ),
]