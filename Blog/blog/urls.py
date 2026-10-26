from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("articulos/<slug:slug>/", views.article_detail, name="article_detail"),
]