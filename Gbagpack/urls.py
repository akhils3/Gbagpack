"""
URL configuration for Gbagpack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home),
    path('shop',views.shop),
    path('blog',views.blog),

    path('contact',views.contact),
    path('contactdata',views.contactdata1),


    path('myaccount',views.myaccount),
    path('forgotpassword',views.forgotpassword1),
    path('signup',views.signup),
    path('blogone',views.blogone),
    path('blogtwo',views.blogtwo),
    path('blogthree',views.blogthree),
    path('blogfour',views.blogfour),
    path('blogfive',views.blogfive),
    path('blogsix',views.blogsix),

]
