from django.shortcuts import render
from Yorking.models import match_user,country_team
from Yorking import form
# Create your views here.
def index(request):
    return render(request,'Yorking/index.html')

def selection(request):
    if request.method=='POST':
        coun1=request.POST.get('country1')
        coun2=request.POST.get('country2')
        countryteamobj=country_team.objects.filter(country__exact=coun1) | country_team.objects.filter(country__exact=coun2)
        return render(request,'Yorking/team_selection.html',{'teamdata':countryteamobj})

def edit_selection(request):
    match_user_obj=match_user.objects.filter(status__exact='Not occured').values('match_id')
    return render(request,'Yorking/edit_selection.html',{'matchcountries':match_user_obj})

def playerperfomance(request):
    return render(request,'Yorking/playerperfomance.html',{})



def djangoform(request):
    form_obj=form.MatchesForm(request.POST)
    if request.method=='POST' and form_obj.is_valid():
        print(form_obj.cleaned_data.get('matchid'))
    else:
        print('form is not valid')
    return render(request,'Yorking/djangoform.html',{'form':form_obj})

def modelform(request):
    if request.method=='POST':
        coun1=request.POST.get('country1')
        coun2=request.POST.get('country2')
        matchuserobj=match_user(country1=coun1,country2=coun2)
        matchuserobj.save()
        select=request.POST.get('select')
        submit=request.POST.get('submit')
        if select == '':
            countryteamobj=country_team.objects.filter(country__exact=coun1) | country_team.objects.filter(country__exact=coun2)
            return render(request,'Yorking/team_selection.html',{'teamdata':countryteamobj})
        elif submit == '':
            return render(request,'Yorking/form.html')
    else:
        return render(request,'Yorking/form.html')
