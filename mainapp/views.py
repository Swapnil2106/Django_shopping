from .models import Product,Category

from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Product, CustomerModel, OrderModel

# Create your views here.


def homepageview(request):
    return render(request, "homepage.html")


def signupuser(request):
    username = request.POST['username']
    password = request.POST['password']
    phoneno = request.POST['phoneno']

    # if user exists
    if User.objects.filter(username=username).exists():
        messages.add_message(request, messages.ERROR, "User already exists")
        return redirect('homepage')
    # if user doesn't exists
    User.objects.create_user(username=username, password=password).save()
    lastobject = len(User.objects.all())-1
    CustomerModel(userid=User.objects.all()[
                  int(lastobject)].id, phoneno=phoneno).save()
    messages.add_message(request, messages.ERROR, "User Successfully created")
    return redirect('homepage')


def userloginview(requset):
    return render(requset, 'userlogin.html')


def userauthenticate(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    # user exists
    if user is not None:
        login(request, user)
        return redirect('customerpage')

    # user doesn't exists
    if user is None:
        messages.add_message(request, messages.ERROR, "Invalid Credentials")
        return redirect('userloginpage')

def mainpage(request):
	username = request.user.username
	context = {'username': username, 'products': Product.objects.all()}
	return render(request, 'mainpage.html', context)

def cart(request):
    username = request.user.username
    context = {'username': username}
    return render(request, 'cart.html',context)    

def customerwelcomeview(request):
    if not request.user.is_authenticated:
        return redirect('userloginpage')
    username = request.user.username
    context = {'username': username, 'products': Product.objects.all()}
    return render(request, 'customerwelcome.html', context)


def userlogout(request):
    logout(request)
    return redirect('userloginpage')


def placeorder(request):
    if not request.user.is_authenticated:
        return redirect('userloginpage')
    username = request.user.username
    phoneno = CustomerModel.objects.filter(userid=request.user.id)[0].phoneno
    address = request.POST['address']
    orderitems = ""
    for product in Product.objects.all():
        productid = product.id
        name = product.name
        price = product.price
        quantity = request.POST.get(str(productid), " ")
        if str(quantity) != "0" and str(quantity) != " ":
            orderitems = orderitems + name + " " + "price :" + \
                str(int(quantity)*int(price)) + " " + \
                "quantity : " + quantity + "    "

    OrderModel(username=username, phoneno=phoneno,
               address=address, orderitems=orderitems).save()
    messages.add_message(request, messages.ERROR,
                         "Order Placed Successfully..!!")
    return redirect('customerpage')


def userorders(request):
    orders = OrderModel.objects.filter(username=request.user.username)
    context = {'orders': orders}
    return render(request, 'userorders.html', context)
