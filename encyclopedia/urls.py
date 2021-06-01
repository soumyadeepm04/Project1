from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.getentry, name = "getentry"),
    path("search", views.search, name = "search")
]
