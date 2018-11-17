from django.shortcuts import render
from organiser_app.forms import *
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def index(request):
    return render(request,'organiser_app/index.html')

def candidate_page(request):
    if request.method=="POST":
        candidate_form=Candidateform(data=request.POST)


        if candidate_form.is_valid():

            candidate_form.save(commit=True)


        else:
            print(user_form.errors,profile_form.errors)

    else:
        candidate_form=Candidateform()


    return render(request,'organiser_app/addcandidate.html',{'candidate_form':candidate_form })
