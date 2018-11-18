from django import forms
from . models import *

region_options=(

 ('0','AndhraPradesh') ,
 ('1','Bihar') ,
 ('2','karnataka'),
 ('3','Tamilnadu' ),
 ('4','Kerela') ,
 ('5','UttarPradesh'),
 ('6','WestBengal') ,
 ('7','MadhyaPradesh') ,
 ('8','Haryana') ,
 ('9','Assam')

)



class Candidateform(forms.ModelForm):
    candidate_dob = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2002)))

    class Meta():
        model=Candidate
        fields=('candidate_id','candidate_name','candidate_fname','candidate_party','candidate_region','candidate_gender','candidate_email','candidate_dob','candidate_aadhar')


class Electionform(forms.ModelForm):
    date_of_start = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2002)))
    date_of_end = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2002)))
    class Meta():
        model=Election

        fields=('election_type','election_year','date_of_start','date_of_end', 'candidates')

class Voterform(forms.ModelForm):

    class Meta():
        model = Voter
        fields = ('voter_id', 'voter_name', 'voter_email', 'voter_dob', 'voter_age', 'voter_aadhar', 'voter_phone', 'isalive', 'voter_gender', 'voter_region')

class RegionForm(forms.Form):
    region_select = forms.ChoiceField(choices=region_options)
