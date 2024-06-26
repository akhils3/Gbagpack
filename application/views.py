from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect, render
from application.models import *
from django.contrib import messages
from application.models import contactinformation



# Create your views here.

def home(request):
    return render(request,"index.html")

def shop(request):
    obj=ShopProduct.objects.all()
    return render(request,'shop.html',{"data":obj})


def blog(request):
    return render(request,"blog.html")
def blogone(request):
    return render(request, "blogone.html")

def blogtwo(request):
    return render(request, "blogtwo.html")

def blogthree(request):
    return render(request, "blogthree.html")

def blogfour(request):
    return render(request, "blogfour.html")

def blogfive(request):
    return render(request, "blogfive.html")

def blogsix(request):
    return render(request, "blogsix.html")


def contact(request):
    return render(request,"contact.html")
def contactdata1(request):
    fn = request.POST['firstname']
    ln = request.POST['lastname']
    emailid = request.POST['emailaddress']
    commentandmessage = request.POST['commentormessage']

    if(fn=="" or ln=="" or emailid=="" or commentandmessage==""):
        messages.warning(request, "Value Can't Be Empty 🫤")
        return render(request, "contact.html")
    else:
        obj = contactinformation(fname=fn,lname=ln,email=emailid,address=commentandmessage)
        obj.save()

        messages.success(request, "Data SuccessFully Sent ...😊")
        return render(request, "contact.html")
    


def myaccount(request):
    return render(request,"myaccount.html")


def signup(request):
    return render(request, "signup.html")

def forgotpassword(request):
    return render(request, "forgotpassword.html")

def registerdata1(request):
    uname = request.POST['name']
    address1 = request.POST['address']
    email1 = request.POST['email']
    phonenumber = request.POST['mobilenumber']
    registerpassword1 = request.POST['registerpassword']

    if(uname=='' or address1=='' or email1=='' or phonenumber=='' or registerpassword1==''):
        messages.error(request, "Value can not be empty🤨 ..")
        return render(request, "signup.html")
    else:
        obj2 = RegisterData1(username=uname,address=address1,email=email1,mobilenumber=phonenumber,password=registerpassword1)
        obj2.save()
    
        messages.success(request, "Profile details stored successfully👍.")
        return render(request, "signup.html")


def logincheck(request):
    username=request.POST['username']
    userpassword=request.POST['userpass']

    obj=RegisterData1.objects.all()

    if(username=='' or userpassword==''):
        messages.warning(request, "value can not empty !")
        return render(request, "myaccount.html")
    else:
        for i in obj:
            if username==i.username and userpassword==i.password:
                messages.success(request, "Login Successfully...😊 ")
                return render(request,'index.html')

    messages.error(request, "User not found ... 😒 ")
    return render(request,'myaccount.html')   


def cart(request):
    obj=CartItem.objects.all()
    return render(request,'cart.html',{'data':obj})

def addtocart(request):
    c=request.GET.get('imge')
    a=request.GET.get('nm')
    b=request.GET.get('price')

    obj=CartItem(productimage=c,productname=a,productprice=b)
    obj.save()
    messages.success(request, "Data SuccessFully Add On Cart Page 😍..")
    
    obj=ShopProduct.objects.all()
    return render(request, "shop.html",{'data':obj})
