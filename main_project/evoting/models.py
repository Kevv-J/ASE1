from django.db import models
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms

class VotersLog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    voterId = models.BigIntegerField(default=0000000000000)
    fullname = models.CharField(max_length=20, default='')
    dob = models.DateField(default='')