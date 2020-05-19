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
    match_user_obj=match_user.objects.filter(status__exact='Not occured')
    return render(request,'Yorking/edit_selection.html',{'matchcountries':match_user_obj})

def playerperfomance(request):
    if request.method=='POST':
        matchid=request.POST.get('matchid')
        match_user_coun1=match_user.objects.filter(match_id__exact=matchid).values('country1')
        match_user_coun2=match_user.objects.filter(match_id__exact=matchid).values('country2')
        batsman1=country_team.objects.filter(country__exact=match_user_coun1) & country_team.objects.filter(category__exact='batsman')
        baller1=country_team.objects.filter(country__exact=match_user_coun1,category__exact='baller')
        wicketkeeper1=country_team.objects.filter(country__exact=match_user_coun1,category__exact='wicketkeeper')
        allrounder1=country_team.objects.filter(country__exact=match_user_coun1,category__exact='allrounder')
        batsman2=country_team.objects.filter(country__exact=match_user_coun2,category__exact='batsman')
        baller2=country_team.objects.filter(country__exact=match_user_coun2,category__exact='baller')
        wicketkeeper2=country_team.objects.filter(country__exact=match_user_coun2,category__exact='wicketkeeper')
        allrounder2=country_team.objects.filter(country__exact=match_user_coun2,category__exact='allrounder')
        return render(request,'Yorking/playerperfomance.html',{'validation':[],'batsman1':batsman1,'baller1':baller1,'wicketkeeper1':wicketkeeper1,'allrounder1':allrounder1,'batsman2':batsman2,'baller2':baller2,'wicketkeeper2':wicketkeeper2,'allrounder2':allrounder2})


def check_constrains(request):
    batsman1=request.POST.getlist('batsman1')
    baller1=request.POST.getlist('baller1')
    wicketkeeper1=request.POST.getlist('wicketkeeper1')
    allrounder1=request.POST.getlist('allrounder1')
    batsman2=request.POST.getlist('batsman2')
    baller2=request.POST.getlist('baller2')
    wicketkeeper2=request.POST.getlist('wicketkeeper2')
    allrounder2=request.POST.getlist('allrounder2')
    if len(batsman1)<4:
        validation.append("Min 4 batsman required in Country 1")
    if len(baller1)<3:
        validation.append("Min 3 ballers required in Country 1")
    if len(wicketkeeper1)<1:
        validation.append("Min 1 wicketkeeper required you got 0 in Country 1")
    if len(allrounder1)<1:
        validation.append("Min 1 allrounder required you got 0 in Country 1")
    if len(batsman1)+len(baller1)+len(wicketkeeper1)+len(allrounder1)<11:
        validation.append("Min 11 players required in Country 1")
    if len(batsman2)<4:
        validation.append("Min 4 batsman required in Country 2")
    if len(baller2)<3:
        validation.append("Min 3 ballers required in Country 2")
    if len(wicketkeeper2)<1:
        validation.append("Min 1 wicketkeeper required you got 0 in Country 2")
    if len(allrounder2)<1:
        validation.append("Min 1 allrounder required you got 0 in Country 2")
    if len(batsman2)+len(baller2)+len(wicketkeeper2)+len(allrounder2)<11:
        validation.append("Min 11 players required in Country 2")
    return render(request,'Yorking/playerperfomance.html',{'validation':validation,'batsman':batsman,'baller':baller,'wicketkeeper':wicketkeeper,'allrounder':allrounder})



def perfomance_update(request):
    lists=request.POST.getlist('player')
    print(lists)
    return render(request,'Yorking/perfomance_update.html',{'players':lists})





#
# def djangoform(request):
#     form_obj=form.MatchesForm(request.POST)
#     if request.method=='POST' and form_obj.is_valid():
#         print(form_obj.cleaned_data.get('matchid'))
#     else:
#         print('form is not valid')
#     return render(request,'Yorking/djangoform.html',{'form':form_obj})

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
