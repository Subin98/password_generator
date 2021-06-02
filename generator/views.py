from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,'generator/home.html')

def viewpassword(request):
    characters=list('qwertyuioplkjhgfdsazxcvbnm')
    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('special'):
        characters.extend(list('!@$%^&*_~\/?><'))
    if request.GET.get('number'):
        characters.extend(list('1234567890'))
    length=int(request.GET.get('length',8))
    thepassword=''
    for x in range(length):
        thepassword+=random.choice(characters)
    return render(request,'generator/password.html',{'pass':thepassword})

def contact(request_):
    return render(request_,'generator/contact.html')
def about(request):
    return render(request,'generator/about.html')
def mystyle(request):
    return render(request,'generator/mycss/mystyle.css')
