from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.contrib.auth.models import User

# class for Login
class NewForm_forSignIn(forms.Form):
    username = forms.CharField(label= "Username", required = True)
    password = forms.CharField(label= "Password", required = True)


# class for Sign up
class NewForm_forSignUp(forms.Form):
    username = forms.CharField(label= "Username", required = True)
    password = forms.CharField(label= "Password", required = True)
    confirmPass = forms.CharField(label= "Confirm Password", required = True)
   
# Create your views here.
def display(request):
    return render(request, "StartUp_Page/startPage.html");


def signIn(request):
    if request.method == "POST":
        form = NewForm_forSignIn(request.POST)
        if form.is_valid:
            usname = form["username"]
            paswrd = form["password"]
            
    return render(request, "StartUp_Page/SigninPage.html", {
        "form": NewForm_forSignIn()
    });


def signUp(request):
    if request.method == "POST":
        form = NewForm_forSignUp(request.POST)
        if form.is_valid:
            usname = form["username"]
            paswrd = form["password"]
            confirmPass = form["confimPass"]
            
    return render(request, "StartUp_Page/signUpPage.html", {
        "form": NewForm_forSignUp()
    });