from django.db import models
from django.contrib.auth.models import User

class Voters_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=20, blank=True)
    voterId = models.BigIntegerField(blank=True, primary_key=True)
    activation = models.CharField(blank=True, max_length=5, default=False)

    def __str__(self):
        return self.user.username

class Pre_Registered_Database(models.Model):
    voterId = models.BigIntegerField(primary_key=True, null=False)
    fullname = models.CharField(max_length=50, null=False)
    date_of_birth = models.DateField(null=False)
    email = models.EmailField(null=False, max_length=50, default='')
    region = models.CharField(null=False, max_length=30)

    def __str__(self):
        return str(self.voterId)

class Organizers_database(models.Model):
    name = models.CharField(null=False, max_length=50)
    email = models.EmailField(null=False, max_length=40)
    username = models.CharField(null=False, max_length=50)
    password = models.CharField(null=False, max_length=30)

    def __str__(self):
        return self.name
