from django.shortcuts import render
from . import models
# Create your views here.
def Home(request):
    # m_p=models.match_performance(match_id='M501',player_id='101',runs = 50,catches=8,wickets=7,category='allrounder')

    m_p.save()
    return render(request,'index.html',{'preethu':'pravalika'})

def form(request):
    return render(request,'form.html')

def TopPerfomance(request):
    m_p_obj=models.match_performance.objects.all()
    s=[]
    bats=models.match_performance.objects.filter(category__exact='batsman').order_by('runs').reverse()[:3]
    baller=models.match_performance.objects.filter(category__exact='baller').order_by('catches').reverse()[:3]
    wicket=models.match_performance.objects.filter(category__exact='wicketkeeper').order_by('wickets').reverse()[:3]
    for i in m_p_obj:
        s.append(i.runs)
        i.runs=i.runs+i.wickets*20+i.catches*20
    allrounder=models.match_performance.objects.filter(category__exact='allrounder').order_by('runs').reverse()[:3]
    for t,i in enumerate(m_p_obj):
        i.runs=s[t]
    return render(request,'TopPerfomance.html',{'x':bats,'y':baller,'z':wicket,'h':allrounder})
