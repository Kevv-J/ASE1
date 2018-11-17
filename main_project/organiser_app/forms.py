from django import forms
from organiser_app.models import *


class Candidateform(forms.ModelForm):
    candidate_dob = forms.DateField(widget=forms.SelectDateWidget())
    class Meta():
        model=Candidate
        fields=('candidate_id','candidate_name','candidate_fname','candidate_party','candidate_region','candidate_gender','candidate_email','candidate_dob','candidate_aadhar')

class Electionform(forms.ModelForm):

    class Meta():
        model=Election
        fields=('election_type','election_id','election_year','date_of_start','date_of_end','status')
