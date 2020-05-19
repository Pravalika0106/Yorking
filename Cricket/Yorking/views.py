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
        match_user_coun1=match_user.objects.filter(match_id__exact=matchid).values('country1')[0]['country1']
        match_user_coun2=match_user.objects.filter(match_id__exact=matchid).values('country2')[0]['country2']
        batsman1=country_team.objects.filter(country__exact=match_user_coun1,category__exact='batsman').values()
        request.session['batsman1']=list(batsman1)
        baller1=country_team.objects.filter(country__exact=match_user_coun1,category__exact='baller').values()
        request.session['baller1']=list(baller1)
        wicketkeeper1=country_team.objects.filter(country__exact=match_user_coun1,category__exact='wicketkeeper').values()
        request.session['wicketkeeper1']=list(wicketkeeper1)
        allrounder1=country_team.objects.filter(country__exact=match_user_coun1,category__exact='allrounder').values()
        request.session['allrounder1']=list(allrounder1)
        batsman2=country_team.objects.filter(country__exact=match_user_coun2,category__exact='batsman').values()
        request.session['batsman2']=list(batsman2)
        baller2=country_team.objects.filter(country__exact=match_user_coun2,category__exact='baller').values()
        request.session['baller2']=list(baller2)
        wicketkeeper2=country_team.objects.filter(country__exact=match_user_coun2,category__exact='wicketkeeper').values()
        request.session['wicketkeeper1']=list(wicketkeeper2)
        allrounder2=country_team.objects.filter(country__exact=match_user_coun2,category__exact='allrounder').values()
        request.session['allrounder2']=list(allrounder2)
        return render(request,'Yorking/playerperfomance.html',{'validation':[],'batsman1':batsman1,'baller1':baller1,'wicketkeeper1':wicketkeeper1,'allrounder1':allrounder1,'batsman2':batsman2,'baller2':baller2,'wicketkeeper2':wicketkeeper2,'allrounder2':allrounder2})
    else:
        return render(request,'Yorking/index.html')

def check_constrains(request):
    batsman1=request.session['batsman1']
    baller1=request.session['baller1']
    wicketkeeper1=request.session['wicketkeeper1']
    allrounder1=request.session['allrounder1']
    batsman2=request.session['batsman2']
    baller2=request.session['baller2']
    wicketkeeper2=request.session['wicketkeeper1']
    allrounder2=request.session['allrounder2']

    batsmanone=request.POST.getlist('batsman1')
    ballerone=request.POST.getlist('baller1')
    wicketkeeperone=request.POST.getlist('wicketkeeper1')
    allrounderone=request.POST.getlist('allrounder1')
    batsmantwo=request.POST.getlist('batsman2')
    ballertwo=request.POST.getlist('baller2')
    wicketkeepertwo=request.POST.getlist('wicketkeeper2')
    allroundertwo=request.POST.getlist('allrounder2')
    validation=[]
    if len(batsmanone)<4:
        validation.append("Min 4 batsman required in Country 1")
    if len(ballerone)<3:
        validation.append("Min 3 ballers required in Country 1")
    if len(wicketkeeperone)<1:
        validation.append("Min 1 wicketkeeper required you got 0 in Country 1")
    if len(allrounderone)<1:
        validation.append("Min 1 allrounder required you got 0 in Country 1")
    if len(batsmanone)+len(ballerone)+len(wicketkeeperone)+len(allrounderone)<11:
        validation.append("Min 11 players required in Country 1")
    if len(batsmantwo)<4:
        validation.append("Min 4 batsman required in Country 2")
    if len(ballertwo)<3:
        validation.append("Min 3 ballers required in Country 2")
    if len(wicketkeepertwo)<1:
        validation.append("Min 1 wicketkeeper required you got 0 in Country 2")
    if len(allroundertwo)<1:
        validation.append("Min 1 allrounder required you got 0 in Country 2")
    if len(batsmantwo)+len(ballertwo)+len(wicketkeepertwo)+len(allroundertwo)<11:
        validation.append("Min 11 players required in Country 2")
    print(validation[0])
    if validation != []:
        return render(request,'Yorking/playerperfomance.html',{'validation':[],'batsman1':batsman1,'baller1':baller1,'wicketkeeper1':wicketkeeper1,'allrounder1':allrounder1,'batsman2':batsman2,'baller2':baller2,'wicketkeeper2':wicketkeeper2,'allrounder2':allrounder2})
    else:
        return render(request,'Yorking/perfomance_update.html',{})


def perfomance_update(request):
    print(lists)
    return render(request,'Yorking/perfomance_update.html',{})





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
