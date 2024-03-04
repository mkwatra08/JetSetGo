from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from datetime import datetime
from travel.models import contact
from django.contrib import messages
def home(request):
    return render(request, 'body.html')
def about(request):
    return render(request,'#about')
def services(request):
    return render(request,'#services')
def blog(request):
    return render(request, 'blog.html')
def portfolio(request):
    return render(request, 'portfolio.html')
def adventure(request):
    return render(request, 'adventure.html')
def team(request):
    return render(request, '#team')
def Contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        texts = request.POST.get('texts')
        Contact = contact(name = name, email = email, texts = texts, date = datetime.today())
        Contact.save()
        messages.success(request, "Message sent Succesfully.")
    return render(request, '#contact')


def signup(request):
    if request.method=="POST":
        name=request.POST['Name']
        email=request.POST['Email']
        password=request.POST['Password']
        #check if user has eneterd correct cREDENTIAL
        user = authenticate(username='email', password='Password')


        myuser=User.object.create_user(name,email,password)

        myuser.save()

        messages.success(request,"Your account has been succesfully created.")

        return redirect('login')

    return render(request, 'signup.html')


def login(request):
    if request.method=="POST":
        email=request.POST['Email']
        password=request.POST['Password']
        #check if user has eneterd correct cREDENTIAL
        user = authenticate(username='email', password='Password')

        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,"authentication/index.html",{'fname':fname})
        else:
            messages.error(request, "Bad Credential!")
            return redirect('home')
    else:
        return render(request, 'login.html')

# Create your views here.
