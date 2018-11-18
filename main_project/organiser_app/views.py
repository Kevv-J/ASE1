from django.shortcuts import render,redirect,get_object_or_404
from . forms import *
from organiser_app.models import *
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def index(request):
    region_select = RegionForm()

    if request.method=="POST":
        form=RegionForm(request.POST)
        region=request.POST.get('region_select')
        candidates=Candidate.objects.filter(candidate_region=region)
        context={'candidates':candidates}
        return render(request,'organiser_app/region_candidate.html',context)
        # print(form['region_select'])

    context = {'region_select':region_select}
    return render(request, 'organiser_app/index.html',context)


def candidate_page(request):

    if request.method =="POST":
        candidate_form=Candidateform(data=request.POST)

        if candidate_form.is_valid():

            candidate_form.save(commit=True)
            return render(request,'organiser_app/index1.html')

        else:
            print(candidate_form.errors)

    else:
        candidate_form=Candidateform()

    return render(request, 'organiser_app/addcandidate.html', {'candidate_form':candidate_form })


def voter_page(request):

    if request.method == 'POST':

        voter_form = Voterform(data=request.POST)

        if voter_form.is_valid():

            voter_form.save(commit=True)

        else:
            print(voter_form.errors)

    else:
        voter_form = Voterform()

    return render(request, 'organiser_app/addvoter.html', {'voter_form':voter_form})

def main_page(request):
    return render(request,'organiser_app/index1.html')

def election(request):
    return render(request,'organiser_app/election.html')


def addelection(request):
    if request.method=="POST":
        addelection_form=Electionform(data=request.POST)



        if addelection_form.is_valid():


            election_instance = addelection_form.save()

            for candidate in election_instance.candidates.all():

                candidate_election_instance = Candidate_election()
                candidate_election_instance.candidate = candidate
                candidate_election_instance.election = election_instance
                candidate_election_instance.save()




            return render(request,'organiser_app/election.html')


        else:
            print(user_form.errors,profile_form.errors)

    else:
        addelection_form=Electionform()


    return render(request,'organiser_app/election_form.html',{'addelection_form':addelection_form })


def candidate_view(request,pk):
    template_name='organiser_app/candidate_detail.html'
    candidate=get_object_or_404(Candidate,pk=pk)
    return render(request,template_name,{'object':candidate})


def candidate_update(request,pk):
    template_name='organiser_app/candidate_form.html'
    candidate=get_object_or_404(Candidate,pk=pk)
    form=Candidateform(request.POST or None,instance=candidate)
    if form.is_valid():
        form.save()

    return render(request,template_name,{'form':form})
