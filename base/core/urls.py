"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *
from vege.views import *

urlpatterns = [
    path('', receipes, name="receipes"),
    path('home/', home, name="home"),
    path('update_total/', update_total, name="update_total"),
    path('create_razorpay_payment_link', create_razorpay_payment_link, name='create_razorpay_payment_link'),
    path('register/', register_page, name="register"),
    path('login/', login_page, name="login_page"),
    path('reset_total/', reset_total, name='reset_total'),
    path('logout/', logout_view, name="logout"),
    path('delete_receipe/<id>/', delete_receipe, name="delete_receipe"),
    path('update_receipe/<id>/', update_receipe, name="update_receipe"),
    path('admin/', admin.site.urls),
]
