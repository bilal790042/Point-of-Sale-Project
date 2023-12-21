from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Product


# Create your views here.
# class for Login
class NewForm_forSignIn(forms.Form):
    username = forms.CharField(label= "Username", required = True)
    password = forms.CharField(label= "Password", required = True)


class productForm(forms.Form):

    product = forms.CharField(label= "product", required = True)
    quantity = forms.IntegerField(label= "quantity", required = True)
    category = forms.CharField(label= "category", required = True)


# class for Sign up
class NewForm_forSignUp(forms.Form):
    username = forms.CharField(label= "Username", required = True)
    password = forms.CharField(label= "Password", required = True)
    confirmPass = forms.CharField(label= "Confirm Password", required = True)
   


def display(request):
    return render(request, "StartUp_Page/startPage.html");

@login_required(login_url = 'StartUp_Page1:login')
def homePage(request):
    return render(request, "Interfaces/index.html")

def product(request):
    if request.method == 'POST':
        form = productForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("{% url 'StartUp_Page1:Product' %}")
    else:
        form = productForm()
    items = Product.objects.all()
    contex = {
        'items': items,
        'form':  form
    }
    return render(request, "Interfaces/product.html", contex)

def prodDelete(request, pk):
    item = Product.objects.get(id = pk)
    if request.method == 'POST':
        item.delete()
        redirect('StartUp_Page1:Product')
    return render(request, "Interfaces/products_delete.html")


def staff(request):
    return render(request, "Interfaces/staff.html", {
        "name": "name is bilal"
    })


def orders(request):
    return render(request, "Interfaces/order.html", {
        "name": "name is bilal"
    })


def profile(request):
    return render(request, "Interfaces/profile.html", {
        "name": "name is bilal"
    })


def signIn(request):
    if request.method == "POST":
        usname = request.POST.get("username")
        pswrd = request.POST.get("password")

        user = authenticate(request, username = usname, password = pswrd)
        if user is not None:
            login(request, user)
            return redirect('StartUp_Page1:homeP')


        #form = NewForm_forSignIn(request.POST)
        #if form.is_valid:
        #   usname = form["username"]
        #    paswrd = form["password"]


    return render(request, "StartUp_Page/SigninPage.html", {
        "form": NewForm_forSignIn()
    });


def signUp(request):
    if request.method == "POST":
        usname = request.POST.get("Username")
        paswrd = request.POST.get("Password")
        confimPass = request.POST.get("confirmPassword")

        if confimPass != paswrd:
            return HttpResponse("Invalid Password not same")

        else:
            usr = User.objects.create_user(usname, paswrd, confimPass)
            usr.save()

            return redirect("StartUp_Page1:login")

            
    return render(request, "StartUp_Page/signUpPage.html");




def logoutFun(request):
    logout(request)
    return redirect('StartUp_Page1:login')