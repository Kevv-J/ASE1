from django.db import models


# Create your models here.
class Gen(models.Model):
    party = models.CharField(max_length=10)
    total = models.IntegerField(default='0')

    def __str__(self):
        return self.party + str(self.total)
