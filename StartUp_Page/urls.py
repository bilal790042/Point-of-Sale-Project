from django.urls import path

from . import views

app_name = "StartUp_Page"
urlpatterns = [
    path("", views.display, name = "display_page"),
    path("Login", views.signIn, name = "Login"),
    path("signUp", views.signUp, name = "signUp")
]