from django.shortcuts import render
from  django.http import HttpResponse
from .models import Gen
# Create your views here.
from django.template import RequestContext
#from django.shortcuts import render_to_response
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io
import matplotlib.pyplot
import matplotlib.pyplot as plt
import numpy as np
import random

def GraphsViewBar(request):
    f=plt.figure()
    x=np.arange(10)
    #h=[100,200,300,500,600,400,200,100]
    #x=[0,1,2,3,4,5,6,7,8,9]
    #x=['BJP','Congress','TRS','DMK','WTF']
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
    #dict1={'response':HttpResponse(buf.getvalue(),content_type='image/png')}
    response=HttpResponse(buf.getvalue(),content_type='image/png')
    #return render(request,'graphs/index.html',context=dict1)
    #return render_to_response('graphs/index.html',{'graph':HttpResponse(buf.getvalue(),content_type='image/png')})
    return response

def index(request):
    List1=Gen.objects.order_by('party')
    dict1={'grp':List1}
    return render(request,'graphs/index2.html',context=dict1)


"""
    partyname = Gen.objects.all()
    votes1=partyname.total
    freq_series = pd.Series.from_array(votes1)
    plt.figure(figsize=(12, 8))
    ax = freq_series.plot(kind='bar')
    ax.set_title('Voting Results')
    ax.set_xlabel('Parties')
    ax.set_ylabel('No: of Votes')
    parties=partyname.party
    ax.set_xticklabels(parties)

    rects = ax.patches

    # Make some labels.
    labels = partyname.total

    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
                ha='center', va='bottom')
    """
