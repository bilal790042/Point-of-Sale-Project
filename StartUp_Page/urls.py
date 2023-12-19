from django.urls import path

from . import views

app_name = "StartUp_Page1"
urlpatterns = [
    path("", views.display, name = "display_page"),
    path("Login", views.signIn, name = "login"),
    path("signUp", views.signUp, name = "sgnUp"),
    path("home", views.homePage, name = "homeP"),
    path("product", views.product, name = "Product"),
    path("orders", views.orders, name = "Orders"),
    path("profile", views.profile, name = "Profile"),
    path("staff", views.staff, name = "Staff"),
    path("logout", views.logoutFun, name = "logout1"),
]