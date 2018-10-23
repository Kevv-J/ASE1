from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def login_page(request):
    return render(request, 'login/login.html')

def register_page(request):
    return render(request, 'register/register.html')

def home(request):
    print("Request Object: {}".format(request.POST))
    voterid = request.POST['voterid']
    fullname = request.POST['fullname']
    dob = str(request.POST['dob'])
    emailid = request.POST['email']
    password = request.POST['pass']
    voterslog = Voterslog.objects.create(voterId=voterid, fullname=fullname, DoB=dob, emailId=emailid, password=password)
    return HttpResponse("Your have been registered successfully.")
