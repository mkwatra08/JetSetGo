from django.shortcuts import render
from datetime import datetime
from travel.models import contact
from django.contrib import messages
def home(request):
    return render(request, 'body.html')
def about(request):
    return render(request,'#about')
def services(request):
    return render(request,'#services')
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
# Create your views here.
