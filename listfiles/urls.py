from django.urls import path
from . import views


app_name = "listfiles"

urlpatterns = [
    path("", views.BulletinListView.as_view(), name="listFilesPage"),
    path("", views.teste, name = "teste")
]