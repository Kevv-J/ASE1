from django.shortcuts import render,redirect,get_object_or_404
from . forms import *
from . models import *
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from  organiser_app.serializers import  CandidateSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status



# Create your views here.

def party(request):
    party_form = PartyForm()
    context = {'party_form':party_form}
    return render(request, 'organiser_app/party.html',context)




def index(request):
    region_form = RegionForm()
    context = {'region_form':region_form}
    return render(request, 'organiser_app/index.html',context)


def srchcandidate(request):
    candidate_id=request.POST.get('Candidateid')
    print(candidate_id)
    object=Candidate.objects.get(candidate_id=candidate_id)
    print(object)
    context = {'object':object}
    return render(request,'organiser_app/candidate_info.html',context)


def candidate_page(request):

    if request.method =="POST":
        candidate_form=Candidateform(request.POST, request.FILES)

        if candidate_form.is_valid():

            candidate_form.save()

            return render(request,'organiser_app/index1.html')

        else:
            print(candidate_form.errors)

    else:
        candidate_form=Candidateform()

    return render(request, 'organiser_app/addcandidate.html', {'candidate_form':candidate_form })

def main_page(request):
    return render(request,'organiser_app/index1.html')


def election(request):
    election_instance=Election.objects.all()
    context={'election_instance':election_instance}
    return render(request,'organiser_app/election.html',context)

# ------------------------------------Voter Code--------------------------------------------


def add_voter(request):

    if request.method == 'POST':

        voter_form = Voterform(data=request.POST)

        if voter_form.is_valid():

                voter_form.save(commit=True)
                message = 'Voter is added successfully!'
                return render(request, 'organiser_app/add_voter.html', {'voter_form': voter_form, 'message': message})

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

    return render(request, 'organiser_app/select_region.html',context=context)


def search_voter(request):

    if request.method == 'POST':
        voterid = request.POST.get('voterid')
        try:
            voter = Voter.objects.get(voter_id=voterid)
            context = {'voter': voter}
            return render(request, 'organiser_app/search_results.html', context=context)
        except:
            message = 'Voter Id "' + str(voterid) + '" does not exist.'
            context = {'message': message}
            return render(request, 'organiser_app/search_results.html', context=context)

    return render(request, 'organiser_app/search_results.html')


def voter_view(request, pk):
    template_name = 'organiser_app/voter_info.html'
    voter=get_object_or_404(Voter, pk=pk)
    return render(request, template_name, {'voter': voter})


def voter_update(request, pk):
    template_name = 'organiser_app/update_voter_form.html'
    voter = get_object_or_404(Voter, pk=pk)
    voter_form = Voterform(request.POST or None, instance=voter)
    if request.method == 'POST':
        if voter_form.is_valid():
            voter_form.save()
            message = 'Voter Id "' + str(voter.voter_id) + '" is updated successfully!'
            return render(request, template_name, {'voter_form': voter_form, 'message': message})
    return render(request, template_name, {'voter_form': voter_form})


#-------------------------------------------End Voter Code--------------------------------------------------


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

            if election_instance.election_type == 'P':
                for i in range(0,10):
                    election_region_instance=Election_region()
                    election_region_instance.region=i
                    election_region_instance.election=election_instance
                    election_region_instance.save()

            if election_instance.election_type=='A':
                election_region_instance=Election_region()
                region=request.POST['statelist']
                election_region_instance.region=region
                election_region_instance.election=election_instance
                election_region_instance.save()


            election_instance=Election.objects.all()
            context={'election_instance':election_instance}
            return render(request,'organiser_app/election.html',context)

        else:
            print(addelection_form.errors)

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
    if request.method=="POST":

        if form.is_valid():
            form.save()
            #return HttpResponseRedirect(reverse( organiser_app:candidate_edit 'form.candidate_id ))

    return render(request,template_name,{'form':form})

def reg_candidate(request,pk):
    template_name='organiser_app/region_candidate.html'
    candidates=Candidate.objects.filter(candidate_region=pk)
    context={'candidates':candidates}
    return render(request,template_name,context)


def party_candidate(request,pk):
    template_name='organiser_app/region_candidate.html'
    candidates=Candidate.objects.filter(candidate_party=pk)
    context={'candidates':candidates}
    return render(request,template_name,context)



def election_candidate(request,pk):
    template_name='organiser_app/region_candidate.html'
    candidates_ele=Candidate_election.objects.filter(election=pk)
    list_candidate=[]
    for candi in candidates_ele:
        list_candidate.append(candi.candidate)
    context={'candidates':list_candidate}
    return render(request,template_name,context)


def candidate_election(request,pk):
    template_name='organiser_app/election.html'
    election_ins=Candidate_election.objects.filter(candidate=pk)
    election_instance=[]
    for ele in election_ins:
        election_instance.append(ele.election)
    context={'election_instance':election_instance}
    return render(request,template_name,context)


def election_update(request,pk):
    template_name='organiser_app/election_update.html'
    election=get_object_or_404(Election,pk=pk)
    form=Electionform(request.POST or None,instance=election)
    if request.method=="POST":
        if form.is_valid():
            form.save()

            election_instance=Election.objects.all()
            context={'election_instance':election_instance}
            return render(request,'organiser_app/election.html',context)

    return render(request,template_name,{'form':form})



class candidateListView(APIView):

    def get(self,request):
        candidate=Candidate.objects.all()
        serializer=CandidateSerializer(candidate,many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer=CandidateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
