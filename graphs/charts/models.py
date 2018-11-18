from django.db import models

# Create your models here.
class Gen(models.Model):
    party = models.CharField(unique=True,max_length=10)
    total = models.IntegerField(default='0')
    def __str__(self):
        return self.party + str(self.total)
class Feedback(models.Model):
    name = models.CharField(max_length=30,null=False)
    feedback = models.CharField(max_length=300,null=False)
    def str(self):
        return self.name
