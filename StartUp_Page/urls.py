from django.urls import path

from . import views

app_name = "StartUp_Page1"
urlpatterns = [
    path("", views.display, name = "display_page"),
    path("Login", views.signIn, name = "login"),
    path("signUp", views.signUp, name = "signUp"),
    path("home", views.homePage, name = "homeP")
]