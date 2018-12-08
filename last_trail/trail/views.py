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
    regions = candidateLog.objects.values_list('region_2', flat=True)
    voterId = voterLog.objects.values_list('voterid', flat=True)

    if region in regions:
        if voterid not in voterId:
          regions=candidateLog.objects.filter(region_2=region)
          candidates=regions.values_list('candidate') #Getting Name
          candidate_ids=regions.values_list('candidate_id') #Getting ID
          a=len(candidates)
          evenlist=[]
          oddlist=[]
          candidates_new=[]
          for i in range(0,len(candidates)):
            candidates_new.append([candidates[i][0],candidate_ids[i][0]])
          result_region={'region':region,'candidates_new':candidates_new,'regions':regions}
          return render(request,"trail/index6.html",result_region)

        else:
         return HttpResponse('Invalid Details!!')


