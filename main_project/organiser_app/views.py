from django.shortcuts import render
from . forms import *
from . models import *
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def index(request):
    return render(request, 'organiser_app/index.html')


def candidate_page(request):

    if request.method =="POST":
        candidate_form=Candidateform(data=request.POST)

        if candidate_form.is_valid():

            candidate_form.save(commit=True)

        else:
            print(candidate_form.errors)

    else:
        candidate_form=Candidateform()

    return render(request, 'organiser_app/addcandidate.html', {'candidate_form':candidate_form })

def main_page(request):
    return render(request,'organiser_app/index1.html')


def election(request):
    return render(request,'organiser_app/election.html')

def addelection(request):
    if request.method=="POST":
        addelection_form=Electionform(data=request.POST)


        if addelection_form.is_valid():

            addelection_form.save(commit=True)


        else:
            print(user_form.errors,profile_form.errors)

    else:
        addelection_form=Electionform()


    return render(request,'organiser_app/election_form.html',{'addelection_form':addelection_form })

# ---------------------------------------------------------------------------------


def add_voter(request):

    if request.method == 'POST':

        voter_form = Voterform(data=request.POST)

        if voter_form.is_valid():

            voter_form.save(commit=True)

        else:
            print(voter_form.errors)
    else:
        voter_form = Voterform()

    return render(request, 'organiser_app/add_voter.html', {'voter_form':voter_form})


def voter_region_page(request):

    region_form = RegionForm()
    context = {'region_form':region_form}
    if request.method == 'POST':
        region = request.POST.get('select_region')
        voters = Voter.objects.filter(voter_region=region)
        return render(request, 'organiser_app/voters_list.html',{'voters':voters})

    return render(request, 'organiser_app/region_page.html',context=context)


def search_voter(request):

    if request.method == 'POST':
        voterid = request.POST.get('voterid')
        print(voterid)
        try:
            voter = Voter.objects.get(voter_id = voterid )
            print(voter.voter_name)
            context = {'voter':voter}
            return render(request,'organiser_app/update_voter.html',context=context)
        except:
            message = 'Voter Id '+ str(voterid) + " does not exist."
            context = {'message' : message}
            return render(request, 'organiser_app/update_voter.html', context=context)

    return render(request,'organiser_app/update_voter.html')



