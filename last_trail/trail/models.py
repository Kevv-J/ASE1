from django.db import models

class voterLog(models.Model):
    fullname = models.CharField(max_length=150,null="True")
    email = models.CharField(max_length=150,null="True")
    region = models.CharField(max_length=150,null="True")
    voterid=models.IntegerField(primary_key=True)

    def __str__(self):
        return self.region


class candidateLog(models.Model):
    candidate_id=models.AutoField(primary_key=True)
    region_2 = models.CharField(max_length=150,null="True")
    candidate = models.CharField(max_length=50,null="True")
    phone_no=models.BigIntegerField(null="true")
    email=models.EmailField(unique=True)
    date_birth=models.DateField(null="true")
    party=models.CharField(max_length=50,null="True")

    def __str__(self):
        return str(self.candidate_id)



