from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    return render(request, "StartUp_Page/startPage.html");


def signIn(request):
    return render(request, "StartUp_Page/SigninPage.html");