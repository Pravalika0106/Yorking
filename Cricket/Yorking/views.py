from django.shortcuts import render
from Yorking.models import match_user,country_team
# Create your views here.
def index(request):
    return render(request,'Yorking/index.html')

def selection(request):
    coun1=request.POST['country1']
    coun2=request.POST['country2']
    countryteamobj=country_team.objects.filter(country__exact=coun1) | country_team.objects.filter(country__exact=coun2)
    return render(request,'Yorking/team_selection.html',{'teamdata':countryteamobj})

def modelform(request):
    if request.method=='POST':
        coun1=request.POST['country1']
        coun2=request.POST['country2']
        matchuserobj=match_user(country1=coun1,country2=coun2)
        matchuserobj.save()
        return render(request,'Yorking/form.html')
    else:
        return render(request,'Yorking/form.html')
