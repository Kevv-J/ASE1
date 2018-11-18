from django.db import models


# Create your models here.
class voterLog(models.Model):
    fullname = models.CharField(max_length=150,null=True)
    email = models.CharField(max_length=150,null=True)
    region = models.CharField(max_length=150,null=True)


class candidateLog(models.Model):
    region_2 = models.CharField(max_length=150,null=True)
    candidate = models.CharField(max_length=50,null=True)
