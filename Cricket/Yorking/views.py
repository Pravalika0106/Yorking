from django.shortcuts import render,redirect
from Yorking.models import match_user,country_team,match_performance,user_team,choosen_players,user
from Yorking import form
from uuid import uuid4
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django .urls import reverse
from django.views.decorators.csrf import csrf_exempt

#Players=country_team,Matches=match_user,User_team=user_team,Choosen_players=choosen_players

#VIEWS HERE

def index(request):
    return render(request,'Yorking/index.html')

def edit_selection(request):
    match_user_obj=match_user.objects.filter(status__exact='Not occured')
    return render(request,'Yorking/edit_selection.html',{'matchcountries':match_user_obj})

def playerperfomance(request):
    if request.method=='POST':
        matchid=request.POST.get('matchid')


        request.session['matchid_edit']=matchid

        match_user_coun1=match_user.objects.filter(match_id__exact=matchid).values('country1')[0]['country1']
        match_user_coun2=match_user.objects.filter(match_id__exact=matchid).values('country2')[0]['country2']
        request.session['countryone']=match_user_coun1
        request.session['countrytwo']=match_user_coun2

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
        return render(request,'Yorking/playerperfomance.html',{'validation':[],'country1':match_user_coun1,'country2':match_user_coun2,'batsman1':batsman1,'baller1':baller1,'wicketkeeper1':wicketkeeper1,'allrounder1':allrounder1,'batsman2':batsman2,'baller2':baller2,'wicketkeeper2':wicketkeeper2,'allrounder2':allrounder2})
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
    sum1=0
    sum2=0
    for i in batsmanone:
        x=country_team.objects.filter(player_id__exact=i).values('points')
        sum1+=x[0]['points']
    for i in ballerone:
        x=country_team.objects.filter(player_id__exact=i).values('points')
        sum1+=x[0]['points']
    for i in wicketkeeperone:
        x=country_team.objects.filter(player_id__exact=i).values('points')
        sum1+=x[0]['points']
    for i in allrounderone:
        x=country_team.objects.filter(player_id__exact=i).values('points')
        sum1+=x[0]['points']

    for i in batsmantwo:
        x=country_team.objects.filter(player_id__exact=i).values('points')
        sum2+=x[0]['points']
    for i in ballertwo:
        x=country_team.objects.filter(player_id__exact=i).values('points')
        sum2+=x[0]['points']
    for i in wicketkeepertwo:
        x=country_team.objects.filter(player_id__exact=i).values('points')
        sum2+=x[0]['points']
    for i in allroundertwo:
        x=country_team.objects.filter(player_id__exact=i).values('points')
        sum2+=x[0]['points']


    validation=[]
    if sum1>100:
        validation.apppend("Total points for Country 1 should be less than 100")
    if len(batsmanone)<1:
        validation.append("Min 1 batsman required in Country 1")
    if len(ballerone)<1:
        validation.append("Min 1 ballers required in Country 1")
    if len(wicketkeeperone)<1:
        validation.append("Min 1 wicketkeeper required you got 0 in Country 1")
    if len(allrounderone)<1:
        validation.append("Min 1 allrounder required you got 0 in Country 1")
    if len(batsmanone)+len(ballerone)+len(wicketkeeperone)+len(allrounderone)<4:
        validation.append("Min 4 players required in Country 1")

    if sum2>100:
        validation.apppend("Total points for Country 2 should be less than 100")
    if len(batsmantwo)<1:
        validation.append("Min 1 batsman required in Country 2")
    if len(ballertwo)<1:
        validation.append("Min 1 ballers required in Country 2")
    if len(wicketkeepertwo)<1:
        validation.append("Min 1 wicketkeeper required you got 0 in Country 2")
    if len(allroundertwo)<1:
        validation.append("Min 1 allrounder required you got 0 in Country 2")
    if len(batsmantwo)+len(ballertwo)+len(wicketkeepertwo)+len(allroundertwo)<4:
        validation.append("Min 4 players required in Country 2")
    if validation != []:
        return render(request,'Yorking/playerperfomance.html',{'validation':validation,'batsman1':batsman1,'baller1':baller1,'wicketkeeper1':wicketkeeper1,'allrounder1':allrounder1,'batsman2':batsman2,'baller2':baller2,'wicketkeeper2':wicketkeeper2,'allrounder2':allrounder2})
    else:
        batsmanone_selected=[]
        ballerone_selected=[]
        wicketkeeperone_selected=[]
        allrounderone_selected=[]
        batsmantwo_selected=[]
        ballertwo_selected=[]
        wicketkeepertwo_selected=[]
        allroundertwo_selected=[]
        for i in batsmanone:
            batsmanone_selected.append(country_team.objects.filter(player_id__exact=i).values('player_id','player_name')[0])
        for i in ballerone:
            ballerone_selected.append(country_team.objects.filter(player_id__exact=i).values('player_id','player_name')[0])
        for i in wicketkeeperone:
            wicketkeeperone_selected.append(country_team.objects.filter(player_id__exact=i).values('player_id','player_name')[0])
        for i in allrounderone:
            allrounderone_selected.append(country_team.objects.filter(player_id__exact=i).values('player_id','player_name')[0])
        for i in batsmantwo:
            batsmantwo_selected.append(country_team.objects.filter(player_id__exact=i).values('player_id','player_name')[0])
        for i in ballertwo:
            ballertwo_selected.append(country_team.objects.filter(player_id__exact=i).values('player_id','player_name')[0])
        for i in wicketkeepertwo:
            wicketkeepertwo_selected.append(country_team.objects.filter(player_id__exact=i).values('player_id','player_name')[0])
        for i in allroundertwo:
            allroundertwo_selected.append(country_team.objects.filter(player_id__exact=i).values('player_id','player_name')[0])

        request.session['batsmanone_selected']=batsmanone_selected
        request.session['ballerone_selected']=ballerone_selected
        request.session['wicketkeeperone_selected']=wicketkeeperone_selected
        request.session['allrounderone_selected']=allrounderone_selected

        request.session['batsmantwo_selected']=batsmantwo_selected
        request.session['ballertwo_selected']=ballertwo_selected
        request.session['wicketkeepertwo_selected']=wicketkeepertwo_selected
        request.session['allroundertwo_selected']=allroundertwo_selected
        return render(request,'Yorking/perfomance_update.html',{'country1':request.session['countryone'],'country2':request.session['countrytwo'],'batsmanone_selected':batsmanone_selected,'ballerone_selected':ballerone_selected,'wicketkeeperone_selected':wicketkeeperone_selected,'allrounderone_selected':allrounderone_selected,'batsmantwo_selected':batsmantwo_selected,'ballertwo_selected':ballertwo_selected,'wicketkeepertwo_selected':wicketkeepertwo_selected,'allroundertwo_selected':allroundertwo_selected})


def perfomance_update(request):

    batsmanone_selected=request.session['batsmanone_selected']
    ballerone_selected=request.session['ballerone_selected']
    wicketkeeperone_selected=request.session['wicketkeeperone_selected']
    allrounderone_selected=request.session['allrounderone_selected']

    batsmantwo_selected=request.session['batsmantwo_selected']
    ballertwo_selected=request.session['ballertwo_selected']
    wicketkeepertwo_selected=request.session['wicketkeepertwo_selected']
    allroundertwo_selected=request.session['allroundertwo_selected']
    return render(request,'Yorking/perfomance_update.html',{'country1':request.session['countryone'],'country2':request.session['countrytwo'],'batsmanone_selected':batsmanone_selected,'ballerone_selected':ballerone_selected,'wicketkeeperone_selected':wicketkeeperone_selected,'allrounderone_selected':allrounderone_selected,'batsmantwo_selected':batsmantwo_selected,'ballertwo_selected':ballertwo_selected,'wicketkeepertwo_selected':wicketkeepertwo_selected,'allroundertwo_selected':allroundertwo_selected})

def perfomance_update_save(request):
    matchid=request.session['matchid_edit']
    batsmanone_selected=request.session['batsmanone_selected']
    ballerone_selected=request.session['ballerone_selected']
    wicketkeeperone_selected=request.session['wicketkeeperone_selected']
    allrounderone_selected=request.session['allrounderone_selected']

    batsmantwo_selected=request.session['batsmantwo_selected']
    ballertwo_selected=request.session['ballertwo_selected']
    wicketkeepertwo_selected=request.session['wicketkeepertwo_selected']
    allroundertwo_selected=request.session['allroundertwo_selected']


    for i in batsmanone_selected:
        playerid=i['player_id']
        runs=request.POST.get('runs'+playerid)
        catches=request.POST.get('catches'+playerid)
        wickets=request.POST.get('wickets'+playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        match_user_obj=match_user.objects.get(match_id__exact=matchid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,runs=runs,catches=catches,wickets=wickets)
        match_performance_obj.save()
    for i in ballerone_selected:
        playerid=i['player_id']
        runs=request.POST.get('runs'+playerid)
        catches=request.POST.get('catches'+playerid)
        wickets=request.POST.get('wickets'+playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        match_user_obj=match_user.objects.get(match_id__exact=matchid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,runs=runs,catches=catches,wickets=wickets)
        match_performance_obj.save()
    for i in wicketkeeperone_selected:
        playerid=i['player_id']
        runs=request.POST.get('runs'+playerid)
        catches=request.POST.get('catches'+playerid)
        wickets=request.POST.get('wickets'+playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        match_user_obj=match_user.objects.get(match_id__exact=matchid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,runs=runs,catches=catches,wickets=wickets)
        match_performance_obj.save()
    for i in allrounderone_selected:
        playerid=i['player_id']
        runs=request.POST.get('runs'+playerid)
        catches=request.POST.get('catches'+playerid)
        wickets=request.POST.get('wickets'+playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        match_user_obj=match_user.objects.get(match_id__exact=matchid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,runs=runs,catches=catches,wickets=wickets)
        match_performance_obj.save()

    for i in batsmantwo_selected:
        playerid=i['player_id']
        runs=request.POST.get('runs'+playerid)
        catches=request.POST.get('catches'+playerid)
        wickets=request.POST.get('wickets'+playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        match_user_obj=match_user.objects.get(match_id__exact=matchid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,runs=runs,catches=catches,wickets=wickets)
        match_performance_obj.save()
    for i in ballertwo_selected:
        playerid=i['player_id']
        runs=request.POST.get('runs'+playerid)
        catches=request.POST.get('catches'+playerid)
        wickets=request.POST.get('wickets'+playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        match_user_obj=match_user.objects.get(match_id__exact=matchid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,runs=runs,catches=catches,wickets=wickets)
        match_performance_obj.save()
    for i in wicketkeepertwo_selected:
        playerid=i['player_id']
        runs=request.POST.get('runs'+playerid)
        catches=request.POST.get('catches'+playerid)
        wickets=request.POST.get('wickets'+playerid)
        match_user_obj=match_user.objects.get(match_id__exact=matchid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,runs=runs,catches=catches,wickets=wickets)
        match_performance_obj.save()
    for i in allroundertwo_selected:
        playerid=i['player_id']
        runs=request.POST.get('runs'+playerid)
        catches=request.POST.get('catches'+playerid)
        wickets=request.POST.get('wickets'+playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        match_user_obj=match_user.objects.get(match_id__exact=matchid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,runs=runs,catches=catches,wickets=wickets)
        match_performance_obj.save()

    match_user.objects.filter(match_id__exact=matchid).update(status='Available')
    return render(request,'Yorking/index.html')


##########OTHER THREAD ALL TOGETHER#######

def modelform(request):
    country_team_obj=country_team.objects.order_by('country').values('country').distinct()
    return render(request,'Yorking/form.html',{'error':[],'countries':country_team_obj})

def form_check(request):
    coun1=request.POST.get('country1')
    coun2=request.POST.get('country2')
    request.session['country_one']=coun1
    request.session['country_two']=coun2
    error=[]
    if coun1 == coun2:
        error.append('Select two different countries')
        country_team_obj=country_team.objects.order_by('country').values('country').distinct()
        return render(request,'Yorking/form.html',{'error':error,'countries':country_team_obj})
    else:

        matchuserobj=match_user(country1=coun1,country2=coun2)
        matchuserobj.save()


        request.session['match_id_created']=matchuserobj.match_id

        select=request.POST.get('select')
        submit=request.POST.get('submit')

        if select == '':
            batsman_1=country_team.objects.filter(country__exact=coun1,category__exact='batsman').values()
            request.session['batsman_1']=list(batsman_1)
            baller_1=country_team.objects.filter(country__exact=coun1,category__exact='baller').values()
            request.session['baller_1']=list(baller_1)
            wicketkeeper_1=country_team.objects.filter(country__exact=coun1,category__exact='wicketkeeper').values()
            request.session['wicketkeeper_1']=list(wicketkeeper_1)
            allrounder_1=country_team.objects.filter(country__exact=coun1,category__exact='allrounder').values()
            request.session['allrounder_1']=list(allrounder_1)
            batsman_2=country_team.objects.filter(country__exact=coun2,category__exact='batsman').values()
            request.session['batsman_2']=list(batsman_2)
            baller_2=country_team.objects.filter(country__exact=coun2,category__exact='baller').values()
            request.session['baller_2']=list(baller_2)
            wicketkeeper_2=country_team.objects.filter(country__exact=coun2,category__exact='wicketkeeper').values()
            request.session['wicketkeeper_1']=list(wicketkeeper_2)
            allrounder_2=country_team.objects.filter(country__exact=coun2,category__exact='allrounder').values()
            request.session['allrounder_2']=list(allrounder_2)
            return render(request,'Yorking/team_selection.html',{'country1':request.session['country_one'],'country2':request.session['country_two'],'validation':[],'batsman_1':batsman_1,'baller_1':baller_1,'wicketkeeper_1':wicketkeeper_1,'allrounder_1':allrounder_1,'batsman_2':batsman_2,'baller_2':baller_2,'wicketkeeper_2':wicketkeeper_2,'allrounder_2':allrounder_2})
        elif submit == '':
            return render(request,'Yorking/index.html')


def selection(request):
    if request.method=='POST':

        coun1=request.POST.get('country1')
        coun2=request.POST.get('country2')

        batsman_1=request.session['batsman_1']
        baller_1=request.session['baller_1']
        wicketkeeper_1=request.session['wicketkeeper_1']
        allrounder_1=request.session['allrounder_1']
        batsman_2=request.session['batsman_2']
        baller_2=request.session['baller_2']
        wicketkeeper_2=request.session['wicketkeeper_1']
        allrounder_2=request.session['allrounder_2']
        validation=request.session['validation']
        return render(request,'Yorking/team_selection.html',{'validation':validation,'batsman_1':batsman_1,'baller_1':baller_1,'wicketkeeper_1':wicketkeeper_1,'allrounder_1':allrounder_1,'batsman_2':batsman_2,'baller_2':baller_2,'wicketkeeper_2':wicketkeeper_2,'allrounder_2':allrounder_2})


def check_constrains_1(request):
    batsman_1=request.session['batsman_1']
    baller_1=request.session['baller_1']
    wicketkeeper_1=request.session['wicketkeeper_1']
    allrounder_1=request.session['allrounder_1']
    batsman_2=request.session['batsman_2']
    baller_2=request.session['baller_2']
    wicketkeeper_2=request.session['wicketkeeper_1']
    allrounder_2=request.session['allrounder_2']


    batsman_one=request.POST.getlist('batsman_1')
    baller_one=request.POST.getlist('baller_1')
    wicketkeeper_one=request.POST.getlist('wicketkeeper_1')
    allrounder_one=request.POST.getlist('allrounder_1')
    batsman_two=request.POST.getlist('batsman_2')
    baller_two=request.POST.getlist('baller_2')
    wicketkeeper_two=request.POST.getlist('wicketkeeper_2')
    allrounder_two=request.POST.getlist('allrounder_2')

    sum1=0
    sum2=0
    for i in batsman_one:
        x=country_team.objects.filter(player_id__exact=i).values('points')
        sum1+=x[0]['points']
    for i in baller_one:
        x=country_team.objects.filter(player_id__exact=i).values('points')
        sum1+=x[0]['points']
    for i in wicketkeeper_one:
        x=country_team.objects.filter(player_id__exact=i).values('points')
        sum1+=x[0]['points']
    for i in allrounder_one:
        x=country_team.objects.filter(player_id__exact=i).values('points')
        sum1+=x[0]['points']

    for i in batsman_two:
        x=country_team.objects.filter(player_id__exact=i).values('points')
        sum2+=x[0]['points']
    for i in baller_two:
        x=country_team.objects.filter(player_id__exact=i).values('points')
        sum2+=x[0]['points']
    for i in wicketkeeper_two:
        x=country_team.objects.filter(player_id__exact=i).values('points')
        sum2+=x[0]['points']
    for i in allrounder_two:
        x=country_team.objects.filter(player_id__exact=i).values('points')
        sum2+=x[0]['points']

    validation=[]
    if sum1>100:
        validation.apppend("Total points for Country 1 should be less than 100")
    if len(batsman_one)<1:
        validation.append("Min 1 batsman required in Country 1")
    if len(baller_one)<1:
        validation.append("Min 1 ballers required in Country 1")
    if len(wicketkeeper_one)<1:
        validation.append("Min 1 wicketkeeper required you got 0 in Country 1")
    if len(allrounder_one)<1:
        validation.append("Min 1 allrounder required you got 0 in Country 1")
    if len(batsman_one)+len(baller_one)+len(wicketkeeper_one)+len(allrounder_one)<4:
        validation.append("Min 4 players required in Country 1")

    if sum2>100:
        validation.append('Total points for Country 2 should be less than 100')
    if len(batsman_two)<1:
        validation.append("Min 1 batsman required in Country 2")
    if len(baller_two)<1:
        validation.append("Min 1 ballers required in Country 2")
    if len(wicketkeeper_two)<1:
        validation.append("Min 1 wicketkeeper required you got 0 in Country 2")
    if len(allrounder_two)<1:
        validation.append("Min 1 allrounder required you got 0 in Country 2")
    if len(batsman_two)+len(baller_two)+len(wicketkeeper_two)+len(allrounder_two)<4:
        validation.append("Min 4 players required in Country 2")
    if validation != []:
        return render(request,'Yorking/team_selection.html',{'country1':request.session['country_one'],'country2':request.session['country_two'],'validation':validation,'batsman_1':batsman_1,'baller_1':baller_1,'wicketkeeper_1':wicketkeeper_1,'allrounder_1':allrounder_1,'batsman_2':batsman_2,'baller_2':baller_2,'wicketkeeper_2':wicketkeeper_2,'allrounder_2':allrounder_2})
    else:
        batsman_one_selected=[]
        baller_one_selected=[]
        wicketkeeper_one_selected=[]
        allrounder_one_selected=[]
        batsman_two_selected=[]
        baller_two_selected=[]
        wicketkeeper_two_selected=[]
        allrounder_two_selected=[]
        for i in batsman_one:
            batsman_one_selected.append(country_team.objects.filter(player_id__exact=i).values('player_id','player_name')[0])
        for i in baller_one:
            baller_one_selected.append(country_team.objects.filter(player_id__exact=i).values('player_id','player_name')[0])
        for i in wicketkeeper_one:
            wicketkeeper_one_selected.append(country_team.objects.filter(player_id__exact=i).values('player_id','player_name')[0])
        for i in allrounder_one:
            allrounder_one_selected.append(country_team.objects.filter(player_id__exact=i).values('player_id','player_name')[0])
        for i in batsman_two:
            batsman_two_selected.append(country_team.objects.filter(player_id__exact=i).values('player_id','player_name')[0])
        for i in baller_two:
            baller_two_selected.append(country_team.objects.filter(player_id__exact=i).values('player_id','player_name')[0])
        for i in wicketkeeper_two:
            wicketkeeper_two_selected.append(country_team.objects.filter(player_id__exact=i).values('player_id','player_name')[0])
        for i in allrounder_two:
            allrounder_two_selected.append(country_team.objects.filter(player_id__exact=i).values('player_id','player_name')[0])

        request.session['batsman_one_selected']=batsman_one_selected
        request.session['baller_one_selected']=baller_one_selected
        request.session['wicketkeeper_one_selected']=wicketkeeper_one_selected
        request.session['allrounder_one_selected']=allrounder_one_selected

        request.session['batsman_two_selected']=batsman_two_selected
        request.session['baller_two_selected']=baller_two_selected
        request.session['wicketkeeper_two_selected']=wicketkeeper_two_selected
        request.session['allrounder_two_selected']=allrounder_two_selected
        return render(request,'Yorking/perfomance_one_update.html',{'country1':request.session['country_one'],'country2':request.session['country_two'],'batsman_one_selected':batsman_one_selected,'baller_one_selected':baller_one_selected,'wicketkeeper_one_selected':wicketkeeper_one_selected,'allrounder_one_selected':allrounder_one_selected,'batsman_two_selected':batsman_two_selected,'baller_two_selected':baller_two_selected,'wicketkeeper_two_selected':wicketkeeper_two_selected,'allrounder_two_selected':allrounder_two_selected})



def perfomance_one_update(request):
    batsman_one_selected=request.session['batsman_one_selected']
    baller_one_selected=request.session['baller_one_selected']
    wicketkeeper_one_selected=request.session['wicketkeeper_one_selected']
    allrounder_one_selected=request.session['allrounder_one_selected']

    batsman_two_selected=request.session['batsman_two_selected']
    baller_two_selected=request.session['baller_two_selected']
    wicketkeeper_two_selected=request.session['wicketkeeper_two_selected']
    allrounder_two_selected=request.session['allrounder_two_selected']
    return render(request,'Yorking/perfomance_one_update.html',{'batsman_one_selected':batsman_one_selected,'baller_one_selected':baller_one_selected,'wicketkeeper_one_selected':wicketkeeper_one_selected,'allrounder_one_selected':allrounder_one_selected,'batsman_two_selected':batsman_two_selected,'baller_two_selected':baller_two_selected,'wicketkeeper_two_selected':wicketkeeper_two_selected,'allrounder_two_selected':allrounder_two_selected})



def perfomance_one_save(request):
    match_id_created=request.session['match_id_created']

    batsman_one_selected=request.session['batsman_one_selected']
    baller_one_selected=request.session['baller_one_selected']
    wicketkeeper_one_selected=request.session['wicketkeeper_one_selected']
    allrounder_one_selected=request.session['allrounder_one_selected']

    batsman_two_selected=request.session['batsman_two_selected']
    baller_two_selected=request.session['baller_two_selected']
    wicketkeeper_two_selected=request.session['wicketkeeper_two_selected']
    allrounder_two_selected=request.session['allrounder_two_selected']

    match_user_obj=match_user.objects.get(match_id__exact=match_id_created)
    for i in batsman_one_selected:
        playerid=i['player_id']
        runs=request.POST.get('runs'+playerid)
        catches=request.POST.get('catches'+playerid)
        wickets=request.POST.get('wickets'+playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,runs=runs,catches=catches,wickets=wickets)
        match_performance_obj.save()
    for i in baller_one_selected:
        playerid=i['player_id']
        runs=request.POST.get('runs'+playerid)
        catches=request.POST.get('catches'+playerid)
        wickets=request.POST.get('wickets'+playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,runs=runs,catches=catches,wickets=wickets)
        match_performance_obj.save()
    for i in wicketkeeper_one_selected:
        playerid=i['player_id']
        runs=request.POST.get('runs'+playerid)
        catches=request.POST.get('catches'+playerid)
        wickets=request.POST.get('wickets'+playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,runs=runs,catches=catches,wickets=wickets)
        match_performance_obj.save()
    for i in allrounder_one_selected:
        playerid=i['player_id']
        runs=request.POST.get('runs'+playerid)
        catches=request.POST.get('catches'+playerid)
        wickets=request.POST.get('wickets'+playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,runs=runs,catches=catches,wickets=wickets)
        match_performance_obj.save()

    for i in batsman_two_selected:
        playerid=i['player_id']
        runs=request.POST.get('runs'+playerid)
        catches=request.POST.get('catches'+playerid)
        wickets=request.POST.get('wickets'+playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,runs=runs,catches=catches,wickets=wickets)
        match_performance_obj.save()
    for i in baller_two_selected:
        playerid=i['player_id']
        runs=request.POST.get('runs'+playerid)
        catches=request.POST.get('catches'+playerid)
        wickets=request.POST.get('wickets'+playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,runs=runs,catches=catches,wickets=wickets)
        match_performance_obj.save()
    for i in wicketkeeper_two_selected:
        playerid=i['player_id']
        runs=request.POST.get('runs'+playerid)
        catches=request.POST.get('catches'+playerid)
        wickets=request.POST.get('wickets'+playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,runs=runs,catches=catches,wickets=wickets)
        match_performance_obj.save()
    for i in allrounder_two_selected:
        playerid=i['player_id']
        runs=request.POST.get('runs'+playerid)
        catches=request.POST.get('catches'+playerid)
        wickets=request.POST.get('wickets'+playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,runs=runs,catches=catches,wickets=wickets)
        match_performance_obj.save()
    match_user.objects.filter(match_id__exact=match_id_created).update(status='Available')
    return render(request,'Yorking/index.html')

def top_performers(request):
    user_id='123'
    return render(request,'Yorking/top_performers.html')







#INTEGRATING SWETHAS CODE HEREE:
#Players=country_team,Matches=match_user,User_team=user_team,Choosen_players=choosen_players







def select_team(request):
    #USER ID FROM USER AUTH PAGE
    # userid=request.session['user_id']###############################################################
    userid=user.objects.all().values()[0]['user_id']
    #RETRIVING THE MATCHES WHICH ARE PLAYED BY THE USER
    user_obj=user.objects.get(user_id=userid)
    user_team_obj=user_team.objects.filter(user_id=user_obj).values('match_id')
    matches=[]
    #RETRIVING THE MATCHES WHO'S STATUS=AVAILABLE
    match_user_obj=match_user.objects.filter(status='Available').values()
    #GETTING THE MATCHES NOT PLAYED BY THE USER
    for i in match_user_obj:
        for j in user_team_obj:
            if i['match_id'] != j['match_id']:
                matches.append(i)
    if len(matches)==0:
        error="No New Matches Available! Come back Later Some time"
    else:
        error=False
    return render(request,'Yorking/team.html',{'error':error,'matches':matches})

def players_list(request):
    if request.method=="POST":
        # POSTED FROM SELECT TEAM
        matchid=request.POST.get("matchid")
        request.session['matchid']= matchid
        coun1=match_user.objects.filter(match_id=matchid).values('country1')[0]['country1']
        coun2 = match_user.objects.filter(match_id=matchid).values('country2')[0]['country2']

        request.session['batsmen'] = list(country_team.objects.filter(country__in=[coun1,coun2],category='batsman').values())
        request.session['all_rounder'] = list(country_team.objects.filter(country__in=[coun1,coun2],category='allrounder').values())
        request.session['bowler'] = list(country_team.objects.filter(country__in=[coun1,coun2],category='baller').values())
        request.session['wicket_keeper']= list(country_team.objects.filter(country__in=[coun1,coun2],category='wicketkeeper').values())

        return  render(request,'Yorking/players.html',{'points':200,'error_msg':[],'batsmen':request.session['batsmen'],'bowler':request.session['bowler'],'all_rounder':request.session['all_rounder'],'wicket_keeper':request.session['wicket_keeper']})
    return render(request,'Yorking/players.html',{'points':points})

def user_team_validation(request):
    selected_batsmen=request.POST.getlist("batsmen")
    selected_bowler = request.POST.getlist("bowler")
    selected_all_rounder = request.POST.getlist("all_rounder")
    selected_wicket_keeper= request.POST.getlist("wicket_keeper")
    error_msg=[]
    selected_points=0

    selected_players = selected_batsmen + selected_bowler+selected_all_rounder + selected_wicket_keeper
    request.session['selected_players']=selected_players


    print("Selected batsman: ", selected_batsmen)
    for i in selected_batsmen:
        selected_points+=country_team.objects.filter(player_id__exact=i)[0].points
    for i in selected_bowler:
        selected_points+=country_team.objects.filter(player_id__exact=i)[0].points
    for i in selected_all_rounder:
        selected_points+=country_team.objects.filter(player_id__exact=i)[0].points
    for i in selected_wicket_keeper:
        selected_points+=country_team.objects.filter(player_id__exact=i)[0].points


    if len(selected_batsmen)<1:
        error_msg.append("select minimum 1 batsmen")
    if len(selected_bowler) < 1:
        error_msg.append("select minimum 1 bowlers")
    if len(selected_wicket_keeper) < 1:
        error_msg.append("select minimum 1 wicket keeper")
    if len(selected_all_rounder) < 1:
        error_msg.append("select minimum 1 all rounder")
    if len(selected_players) < 4:
        error_msg.append("select 4 players")
    if selected_points>200:
        error_msg.append("Select players with points less than 100")
    if error_msg != []:
        return  render(request,'Yorking/players.html',{'points':200,'error_msg':error_msg,'batsmen':request.session['batsmen'],'bowler':request.session['bowler'],'all_rounder':request.session['all_rounder'],'wicket_keeper':request.session['wicket_keeper']})

    else:

        batsmen_selected=[]
        bowler_selected=[]
        all_rounder_selected=[]
        wicket_keeper_selected=[]
        for i in selected_batsmen:
            batsmen_selected.append(country_team.objects.filter(player_id__exact=i).values('player_id','player_name')[0])
        for i in selected_bowler:
            bowler_selected.append(country_team.objects.filter(player_id__exact=i).values('player_id','player_name')[0])
        for i in selected_wicket_keeper:
            wicket_keeper_selected.append(country_team.objects.filter(player_id__exact=i).values('player_id','player_name')[0])
        for i in selected_all_rounder:
            all_rounder_selected.append(country_team.objects.filter(player_id__exact=i).values('player_id','player_name')[0])

        print('else for loop',bowler_selected)
        return render(request,'Yorking/user_team.html',{'batsmen':batsmen_selected,'bowler':bowler_selected,'all_rounder':all_rounder_selected,'wicket_keeper':wicket_keeper_selected})


def dashboard(request):
    captain_id = request.POST["captain"]
    #MATCH ID POSTED FROM SELECT TEAM
    match_user_obj = match_user.objects.get(match_id = request.session['matchid'])

    #USER ID FROM USER AUTH PAGE
    # userid=request.session['user_id']##############################################################
    userid=user.objects.all().values()[0]['user_id']
    user_obj=user.objects.get(user_id__exact=userid)
    user_team_obj = user_team(user_id =user_obj ,match_id = match_user_obj,captain = captain_id)
    user_team_obj.save()
    user_match = user_team.objects.get(match_id = request.session['matchid'],user_id = user_obj)
    for i in request.session['selected_players']:
        country_team_obj= country_team.objects.get(player_id = i)
        choosen_players_obj = choosen_players(user_match = user_match,player_id= country_team_obj )
        choosen_players_obj.save()



    matchid=request.session['matchid']
    match_user_obj=match_user.objects.get(match_id=matchid)

    # user_obj=user.objects.get(user_id=request.session['user_id'])####################################3
    user_obj=user.objects.get(user_id=user.objects.all().values()[0]['user_id'])
    user_team_obj=user_team.objects.get(user_id=user_obj,match_id=match_user_obj)
    user_team_cap=user_team.objects.filter(user_id=user_obj,match_id=match_user_obj).values()[0]['captain']
    choosen_players_obj=choosen_players.objects.filter(user_match=user_team_obj).values()

    match_performance_obj=match_performance.objects.filter(match_id=match_user_obj).values()
    sum=0
    for i in choosen_players_obj:
        for j in match_performance_obj:
            if i['player_id_id']==j['player_id_id']:
                runs=j['runs']
                catches=j['catches']
                wickets=j['wickets']
                sum=sum+runs+(catches*20)+(wickets*20)
    user_team_obj=user_team.objects.filter(user_id=user_obj,match_id=match_user_obj).update(stars=sum)
    return render(request,'Yorking/index.html')



def test(request):
    return redirect(index)


#INTEGRATING ABHIGNA'S CODE HERE:
# Match=match_user,User=user,UserTeam=user_team,MatchPerformance=match_performance,CountryTeam country_team

#INSTEAD OF CALCULATING IT SEPERATELY IT IS DONE CONTINUOUSLY AFTER THE PLAYERS ARE SELECTED

# def user_point_calculation():
#     #MATCH ID POSTED FROM SELECT TEAM
#     matchid=request.POST['matchid']
#     match_user_obj=match_user.objects.get(match_id=matchid)
#
#     user_obj=user.objects.get(user_id=request.session['user_id'])
#
#     user_team_obj=user_team.objects.get(user_id=user_obj,match_id=match_user_obj)
#     user_team_cap=user_team.objects.filter(user_id=user_obj,match_id=match_user_obj).values()[0]['captain']
#     choosen_players_obj=choosen_players.objects.filter(user_match=user_team_obj).values()
#
#     match_performance_obj=match_performance.objects.filter(match_id=match_user_obj).values()
#     sum=0
#     for i in choosen_players_obj:
#         for j in match_performance_obj:
#             if i['player_id_id']==j['player_id_id']:
#                 runs=j['runs']
#                 catches=j['catches']
#                 wickets=j['wickets']
#                 sum=sum+runs+(catches*20)+(wickets*20)
#     user_team_obj=user_team.objects.filter(user_id=user_obj,match_id=match_user_obj).update(stars=sum)
#     return redirect('leaderboard_match')

def leaderboard_match(request):
    #USER ID FORM USER AUTH PAGE
    # user_obj=user.objects.get(user_id__exact=request.session['user_id'])##############################################
    user_obj=user.objects.get(user_id__exact=user.objects.all().values()[0]['user_id'])
    user_matches_played=user_team.objects.filter(user_id_id=user_obj).values()


    matches_leaderboard=[]
    for i in user_matches_played:
        matches_leaderboard.append(match_user.objects.filter(match_id=i['match_id_id']).values()[0])
    return render(request,'Yorking/leaderboard_match.html',{'matches_leaderboard':matches_leaderboard})###Send the data hereee


def leaderboard(request):
    if request.method=='POST':
        matchid=request.POST.get('matchid')
        match_user_obj=match_user.objects.get(match_id__exact=matchid)#display a page to the user and ask him to choose
        user_team_obj=user_team.objects.filter(match_id=match_user_obj).values().order_by('-stars')
        total=len(user_team_obj)
        rank=range(1,total+1)
        lb_data=zip(rank,user_team_obj)
        return render(request,'Yorking/leaderboard.html',{'leaderboard':lb_data})



# def User_Auth(request):
#     forms = form.User_Authentication()
#     if request.method=='POST':
#         forms = form.User_Authentication(request.POST)
#         if forms.is_valid():
#             request.session['user_id']=forms.cleaned_data['user_id']
#             return render(request,'Yorking/index.html')
#     return render(request,'Yorking/User_Auth.html',{"form":forms})


def signup(request):
    if request.method=='POST':
        userid=request.POST.get('user_id')
        password_form=request.POST.get('password')
        user_obj=user.objects.all().values()
        for i in user_obj:
            if userid ==i['user_id']:
                return render(request,'Yorking/signup.html',{'valid':True})
        user_obj_created=user(user_id=userid,password=password_form)
        user_obj_created.save()
        return render(request,'Yorking/index.html')
    return render(request,'Yorking/signup.html',{'valid':False})


def login(request):
    if request.method=='POST':
        userid=request.POST.get('user_id')
        password_form=request.POST.get('password')
        user_obj=user.objects.all().values()
        flag1=0
        flag2=0
        error=[]
        for i in user_obj:
            if i['user_id']==userid:
                flag1=1
                if i['password']==password_form:
                    flag2=1
        if flag1==0:
            error.append('Please check your user id')
        if flag2==0:
            error.append('Please check password')
        if error !=[]:
            return render(request,'Yorking/user_login.html',{'error':error})
        return render(request,'Yorking/index.html')
    return render(request,'Yorking/user_login.html',{'error':False})
