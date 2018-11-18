from django.shortcuts import render
from  django.http import HttpResponse
from .models import Gen,Feedback
# Create your views here.
from django.template import RequestContext
#from django.shortcuts import render_to_response
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io
import matplotlib.pyplot
import matplotlib.pyplot as plt
import numpy as np
import random
def feedback(request):
    return render(request,"graphs/feedback.html")
def form(request):
    return render(request,"graphs/index3.html")
def get_feedback(request):
    print("Request Object: {}".format(request.POST))
    name = request.POST['name1']
    feedback = request.POST['feedback']
    FeedbackData = Feedback.objects.create(name=name, feedback=feedback)
    FeedbackData.save()
    return HttpResponse("Thanks for your feedback")
def index1(request):
    print("Request Object: {}".format(request.POST))
    party = request.POST['party']
    total = request.POST['total']
    Userlog = Gen.objects.create(party=party, total=total)
    Userlog.save()
    return HttpResponse("Your data is stored")

def GraphsViewBar(request):
    f=plt.figure()
    x=np.arange(10)
    c=['Blue','Red','mediumseagreen','goldenrod','deeppink','navy','maroon']
    partyname=Gen.objects.all()
    bar=[]
    n=len(partyname)
    plt.title('Voting Results')
    #plt.xlim(0,10)
    #plt.ylim(0,8)
    plt.xlabel('Parties')
    plt.ylabel('No: of votes')
    y=-1
    for i in range(0,n):
        x=random.randrange(0,6)
        if y==x & y<6:
            x=x+1
        elif y==x & y>0:
            x=x-1
        bar=plt.bar(partyname[i].party,partyname[i].total,width=0.4,color=c[x],linewidth=1.0)
        y=x
    #bar3=plt.bar('Congress',h[2],width=1.0,bottom=0,color='Green')

    plt.legend()

    canvas=FigureCanvasAgg(f)
    buf=io.BytesIO()
    plt.savefig(buf,format='png')
    plt.close(f)
    response=HttpResponse(buf.getvalue(),content_type='image/png')
    return response

def index(request):
    List1=Gen.objects.order_by('party')
    dict1={'grp':List1}
    return render(request,'graphs/index2.html',context=dict1)
