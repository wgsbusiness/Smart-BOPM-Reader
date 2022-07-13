from django.urls import path
from . import views


app_name = "users"

urlpatterns = [
    path("", views.HomePageUsersView.as_view(), name="usersView"),
    path('', views.list_view, name='users'),
]
