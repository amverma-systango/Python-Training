from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name="Index"),
    path('login', views.Login.as_view(), name="Login"),
    path('signup', views.Signup.as_view(), name="Signup"),
]