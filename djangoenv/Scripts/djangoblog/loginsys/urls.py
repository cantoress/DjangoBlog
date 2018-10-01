from django.urls import path, include, re_path
from loginsys import views


urlpatterns = [
    path(r'login/', views.login),
    path(r'logout/', views.logout),
    path(r'register/', views.register),
]
