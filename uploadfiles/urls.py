from django.urls import path
from . import views


app_name = "uploadfiles"

urlpatterns = [
    path("", views.uploadfilesPageView.as_view(), name="uploadfilesPage"),
    path("", views.uploadfilesPageResposta.as_view(), name="uploadfilesPageResposta"),
    path('uploadfiles/', views.uploadFile, name='uploadFile'),
]
