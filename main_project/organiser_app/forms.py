from django import forms
from . models import Candidate,Voter,Election


region_options=(

 ('0','AndhraPradesh'),
 ('1','Bihar'),
 ('2','karnataka'),
 ('3','Tamilnadu'),
 ('4','Kerela'),
 ('5','UttarPradesh'),
 ('6','WestBengal'),
 ('7','MadhyaPradesh'),
 ('8','Haryana'),
 ('9','Assam')

)


class Candidateform(forms.ModelForm):
    candidate_dob = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2002)))

    class Meta:
        model = Candidate
        fields = ('candidate_id','candidate_name','candidate_fname','candidate_party','candidate_region','candidate_gender','candidate_email','candidate_dob','candidate_aadhar')


class Electionform(forms.ModelForm):
    date_of_start = forms.DateField(widget=forms.SelectDateWidget(years=range(2015, 2020)))
    date_of_end = forms.DateField(widget=forms.SelectDateWidget(years=range(2015, 2020)))

    class Meta():
        model=Election
        fields=('election_type','election_year','date_of_start','date_of_end', 'candidates')


class Voterform(forms.ModelForm):
    voter_dob = forms.DateField(
        widget=forms.DateInput(

            attrs={
                'id': 'date',
                'name': 'dob',
                'placeholder': 'YYYY/MM/DD',
                'type': 'date',
            }
        )
    )
    voter_age = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'id': 'age',
                'placeholder': 'Voter Age',

            }
        )
    )

    class Meta:
        model = Voter
        fields = '__all__'


class RegionForm(forms.Form):
    select_region = forms.ChoiceField(choices=region_options)
