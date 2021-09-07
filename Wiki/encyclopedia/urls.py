from django.urls import path

from . import views

urlpatterns = [
    path("wiki", views.index, name="index"),
    path("wiki/search_results", views.search, name = "search"),
    path("wiki/<str:name>", views.topic, name="topic"),
    path("wiki/edit/<str:name>",views.edit, name = "edit")
]
