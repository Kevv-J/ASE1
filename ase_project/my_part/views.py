from django.shortcuts import render, redirect
from .models import voterLog, candidateLog
from django.http import HttpResponse

# Create your views here.


def voter(request):
    return render(request, "my_part/index.html")



