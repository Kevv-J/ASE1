from django.shortcuts import render, redirect, get_object_or_404
from .models import voterLog, candidateLog
from django.http import HttpResponse

# Create your views here.


def voter(request):
    return render(request, "trail/index1.html")


def candidate(request):
    return render(request, "trail/index2.html")


def candidate_details(request,pk):
    template_name='trail/candidate_detail.html'
    candidate=get_object_or_404(candidateLog,pk=pk)
    return render(request,template_name,{'object':candidate})


def result(request):

    region = request.POST.get('region', False)
    voterid=request.POST.get('voterid',False)
    email = request.POST.get('email', False)
    regions = candidateLog.objects.values_list('region_2', flat=True)
    voterId = voterLog.objects.values_list('voterid', flat=True)

    if region in regions:
        if voterid not in voterId:
          regions=candidateLog.objects.filter(region_2=region)
          candidates=list(regions.values_list('candidate'))
          emails = list(regions.values_list('email'))
          phonenumbers = list(regions.values_list('phone_no'))
          parties = list(regions.values_list('party'))
          candidate_ids=list(regions.values_list('candidate_id'))
          dates=list(regions.values_list('date_birth'))
          mylist=[]
          for index in range(len(emails)):
              mylist.append([candidates[index][0], emails[index][0],region,parties[index][0],phonenumbers[index][0],dates[index][0]])
          a=len(candidates)
          evenlist=[]
          oddlist=[]
          candidates_new=[]
          for i in range(0,len(candidates)):
            candidates_new.append([candidates[i][0],candidate_ids[i][0]])
          for i in range(0,len(candidates)):
              if (i%2==0):
                  evenlist.append(candidates_new[i])

              else:
                  oddlist.append(candidates_new[i])

          result_region={'region':region,'oddlist':oddlist,'evenlist':evenlist,'mylist':mylist,'candidates_new':candidates_new}
          return render(request,"trail/index5.html",result_region)

    else:
        return HttpResponse('Invalid Details!!')


def otherpage(request):

    return render(request,'trail/index6.html')

