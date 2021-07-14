from django.contrib import admin
from django.urls import path
from .views import customerwelcomeview, homepageview, placeorder, signupuser, userauthenticate, userloginview, userlogout, userorders,mainpage,cart

urlpatterns = [

    path('', homepageview, name='homepage'),
    path('signupuser/', signupuser),
    path('loginuser/', userloginview, name='userloginpage'),
    path('customer/authenticate/', userauthenticate),
    path('customer/welcome/', customerwelcomeview, name='customerpage'),
    path('userlogout/', userlogout),
    path('placeorder/', placeorder),
    path('userorders/', userorders),
    path('mainpage/',mainpage),
    path('cart/',cart),
]