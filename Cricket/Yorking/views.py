from django.shortcuts import render,redirect
from Yorking.models import match_user,country_team,match_performance,user_team,choosen_players
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

        for i in batsmanone:
            batsmanone_selected=country_team.objects.filter(player_id__exact=i).values('player_id','player_name')
        for i in ballerone:
            ballerone_selected=country_team.objects.filter(player_id__exact=i).values('player_id','player_name')
        for i in wicketkeeperone:
            wicketkeeperone_selected=country_team.objects.filter(player_id__exact=i).values('player_id','player_name')
        for i in allrounderone:
            allrounderone_selected=country_team.objects.filter(player_id__exact=i).values('player_id','player_name')
        for i in batsmantwo:
            batsmantwo_selected=country_team.objects.filter(player_id__exact=i).values('player_id','player_name')
        for i in ballertwo:
            ballertwo_selected=country_team.objects.filter(player_id__exact=i).values('player_id','player_name')
        for i in wicketkeepertwo:
            wicketkeepertwo_selected=country_team.objects.filter(player_id__exact=i).values('player_id','player_name')
        for i in allroundertwo:
            allroundertwo_selected=country_team.objects.filter(player_id__exact=i).values('player_id','player_name')

        request.session['batsmanone_selected']=list(batsmanone_selected)
        request.session['ballerone_selected']=list(ballerone_selected)
        request.session['wicketkeeperone_selected']=list(wicketkeeperone_selected)
        request.session['allrounderone_selected']=list(allrounderone_selected)

        request.session['batsmantwo_selected']=list(batsmantwo_selected)
        request.session['ballertwo_selected']=list(ballertwo_selected)
        request.session['wicketkeepertwo_selected']=list(wicketkeepertwo_selected)
        request.session['allroundertwo_selected']=list(allroundertwo_selected)
        return render(request,'Yorking/perfomance_update.html',{'batsmanone_selected':batsmanone_selected,'ballerone_selected':ballerone_selected,'wicketkeeperone_selected':wicketkeeperone_selected,'allrounderone_selected':allrounderone_selected,'batsmantwo_selected':batsmantwo_selected,'ballertwo_selected':ballertwo_selected,'wicketkeepertwo_selected':wicketkeepertwo_selected,'allroundertwo_selected':allroundertwo_selected})


def perfomance_update(request):

    batsmanone_selected=request.session['batsmanone_selected']
    ballerone_selected=request.session['ballerone_selected']
    wicketkeeperone_selected=request.session['wicketkeeperone_selected']
    allrounderone_selected=request.session['allrounderone_selected']

    batsmantwo_selected=request.session['batsmantwo_selected']
    ballertwo_selected=request.session['ballertwo_selected']
    wicketkeepertwo_selected=request.session['wicketkeepertwo_selected']
    allroundertwo_selected=request.session['allroundertwo_selected']
    return render(request,'Yorking/perfomance_update.html',{'batsmanone_selected':batsmanone_selected,'ballerone_selected':ballerone_selected,'wicketkeeperone_selected':wicketkeeperone_selected,'allrounderone_selected':allrounderone_selected,'batsmantwo_selected':batsmantwo_selected,'ballertwo_selected':ballertwo_selected,'wicketkeepertwo_selected':wicketkeepertwo_selected,'allroundertwo_selected':allroundertwo_selected})

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
        runs=request.POST.get(playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        match_user_obj=match_user.objects.get(match_id__exact=matchid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,runs=runs)
        match_performance_obj.save()
    for i in ballerone_selected:
        playerid=i['player_id']
        catches=request.POST.get(playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        match_user_obj=match_user.objects.get(match_id__exact=matchid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,catches=catches)
        match_performance_obj.save()
    for i in wicketkeeperone_selected:
        playerid=i['player_id']
        wickets=request.POST.get(playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        match_user_obj=match_user.objects.get(match_id__exact=matchid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,wickets=wickets)
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
        runs=request.POST.get(playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        match_user_obj=match_user.objects.get(match_id__exact=matchid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,runs=runs)
        match_performance_obj.save()
    for i in ballertwo_selected:
        playerid=i['player_id']
        catches=request.POST.get(playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        match_user_obj=match_user.objects.get(match_id__exact=matchid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,catches=catches)
        match_performance_obj.save()
    for i in wicketkeepertwo_selected:
        playerid=i['player_id']
        wickets=request.POST.get(playerid)
        match_user_obj=match_user.objects.get(match_id__exact=matchid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,wickets=wickets)
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
    error=[]
    if coun1 == coun2:
        error.append('Select two different countries')
        country_team_obj=country_team.objects.order_by('country').values('country').distinct()
        return render(request,'Yorking/form.html',{'error':error,'countries':country_team_obj})
    else:

        matchuserobj=match_user(country1=coun1,country2=coun2)
        matchuserobj.save()


        request.session['match_id_created']=matchuserobj.match_id
        print(request.session['match_id_created'])
        print('In form check printing match id created')


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
            return render(request,'Yorking/team_selection.html',{'validation':[],'batsman_1':batsman_1,'baller_1':baller_1,'wicketkeeper_1':wicketkeeper_1,'allrounder_1':allrounder_1,'batsman_2':batsman_2,'baller_2':baller_2,'wicketkeeper_2':wicketkeeper_2,'allrounder_2':allrounder_2})
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
        return render(request,'Yorking/team_selection.html',{'validation':validation,'batsman_1':batsman_1,'baller_1':baller_1,'wicketkeeper_1':wicketkeeper_1,'allrounder_1':allrounder_1,'batsman_2':batsman_2,'baller_2':baller_2,'wicketkeeper_2':wicketkeeper_2,'allrounder_2':allrounder_2})
    else:
        for i in batsman_one:
            batsman_one_selected=country_team.objects.filter(player_id__exact=i).values('player_id','player_name')
        for i in baller_one:
            baller_one_selected=country_team.objects.filter(player_id__exact=i).values('player_id','player_name')
        for i in wicketkeeper_one:
            wicketkeeper_one_selected=country_team.objects.filter(player_id__exact=i).values('player_id','player_name')
        for i in allrounder_one:
            allrounder_one_selected=country_team.objects.filter(player_id__exact=i).values('player_id','player_name')
        for i in batsman_two:
            batsman_two_selected=country_team.objects.filter(player_id__exact=i).values('player_id','player_name')
        for i in baller_two:
            baller_two_selected=country_team.objects.filter(player_id__exact=i).values('player_id','player_name')
        for i in wicketkeeper_two:
            wicketkeeper_two_selected=country_team.objects.filter(player_id__exact=i).values('player_id','player_name')
        for i in allrounder_two:
            allrounder_two_selected=country_team.objects.filter(player_id__exact=i).values('player_id','player_name')

        request.session['batsman_one_selected']=list(batsman_one_selected)
        request.session['baller_one_selected']=list(baller_one_selected)
        request.session['wicketkeeper_one_selected']=list(wicketkeeper_one_selected)
        request.session['allrounder_one_selected']=list(allrounder_one_selected)

        request.session['batsman_two_selected']=list(batsman_two_selected)
        request.session['baller_two_selected']=list(baller_two_selected)
        request.session['wicketkeeper_two_selected']=list(wicketkeeper_two_selected)
        request.session['allrounder_two_selected']=list(allrounder_two_selected)
        return render(request,'Yorking/perfomance_one_update.html',{'batsman_one_selected':batsman_one_selected,'baller_one_selected':baller_one_selected,'wicketkeeper_one_selected':wicketkeeper_one_selected,'allrounder_one_selected':allrounder_one_selected,'batsman_two_selected':batsman_two_selected,'baller_two_selected':baller_two_selected,'wicketkeeper_two_selected':wicketkeeper_two_selected,'allrounder_two_selected':allrounder_two_selected})



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
    print(match_id_created)
    print('printing the one received at perfomance one checked')

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
        runs=request.POST.get(playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,runs=runs)
        match_performance_obj.save()
    for i in baller_one_selected:
        playerid=i['player_id']
        catches=request.POST.get(playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,catches=catches)
        match_performance_obj.save()
    for i in wicketkeeper_one_selected:
        playerid=i['player_id']
        wickets=request.POST.get(playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,wickets=wickets)
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
        runs=request.POST.get(playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,runs=runs)
        match_performance_obj.save()
    for i in baller_two_selected:
        playerid=i['player_id']
        catches=request.POST.get(playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,catches=catches)
        match_performance_obj.save()
    for i in wicketkeeper_two_selected:
        playerid=i['player_id']
        wickets=request.POST.get(playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,wickets=wickets)
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
    global points
    points =100
    match_user_obj=match_user.objects.filter(status__exact='Not occured').values()
    if len(match_user_obj)==0:
        error="No Matches Available! Come back Later Some time"
    else:
        error=False
    return render(request,'Yorking/team.html',{'error':error,'matches':match_user_obj})

points =100
def players_list(request):
    if request.method=="POST":
        # POSTED FROM SELECT TEAM
        matchid=request.POST.get("matchid")
        request.session['matchid']= matchid
        print("printing in playerlist",matchid)
        coun1=match_user.objects.filter(match_id=matchid).values('country1')[0]['country1']
        coun2 = match_user.objects.filter(match_id=matchid).values('country2')[0]['country2']
        request.session['batsmen'] = list(country_team.objects.filter(country__in=[coun1,coun2],category='batsman').values())
        request.session['all_rounder'] = list(country_team.objects.filter(country__in=[coun1,coun2],category='allrounder').values())
        request.session['bowler'] = list(country_team.objects.filter(country__in=[coun1,coun2],category='baller').values())
        request.session['wicket_keeper']= list(country_team.objects.filter(country__in=[coun1,coun2],category='wicketkeeper').values())
        # print(request.session['batsmen'])
        return  render(request,'Yorking/players.html',{'points':points,'error_msg':[],'batsmen':request.session['batsmen'],'bowler':request.session['bowler'],'all_rounder':request.session['all_rounder'],'wicket_keeper':request.session['wicket_keeper']})
    return render(request,'Yorking/players.html',{'points':points})

def user_team_validation(request):
    selected_batsmen=request.POST.getlist("batsmen")
    selected_bowler = request.POST.getlist("bowler")
    selected_all_rounder = request.POST.getlist("all_rounder")
    selected_wicket_keeper= request.POST.getlist("wicket_keeper")
    error_msg=[]
    selected_points=0
    print("selected barsman here",selected_batsmen)
    print(len(selected_batsmen))
    selected_players = selected_batsmen + selected_bowler+selected_all_rounder + selected_wicket_keeper
    for i in selected_batsmen:
        selected_points+=country_team.objects.filter(player_id=i)[0].points
    for i in selected_bowler:
        selected_points+=country_team.objects.filter(player_id=i)[0].points
    for i in selected_all_rounder:
        selected_points+=country_team.objects.filter(player_id=i)[0].points
    for i in selected_wicket_keeper:
        selected_points+=country_team.objects.filter(player_id=i)[0].points
    if len(selected_batsmen)<1:
        error_msg.append("select minimum 4 batsmen")
    if len(selected_bowler) < 1:
        error_msg.append("select minimum 3 bowlers")
    if len(selected_wicket_keeper) < 1:
        error_msg.append("select minimum 1 wicket keeper")
    if len(selected_all_rounder) < 1:
        error_msg.append("select minimum 1 all rounder")
    if len(selected_players) < 4:
        error_msg.append("select 11 players")
    if selected_points>200:
        error_msg.append("Select players with points less than 100")
    if error_msg != []:
        return  render(request,'Yorking/players.html',{'points':200,'error_msg':error_msg,'batsmen':request.session['batsmen'],'bowler':request.session['bowler'],'all_rounder':request.session['all_rounder'],'wicket_keeper':request.session['wicket_keeper']})

    else:
        for i in selected_batsmen:
            batsman_selected=country_team.objects.filter(player_id__exact=i).values('player_id','player_name')
        for i in selected_bowler:
            bowler_selected=country_team.objects.filter(player_id__exact=i).values('player_id','player_name')
        for i in selected_wicket_keeper:
            wicket_keeper_selected=country_team.objects.filter(player_id__exact=i).values('player_id','player_name')
        for i in selected_all_rounder:
            all_rounder_selected=country_team.objects.filter(player_id__exact=i).values('player_id','player_name')
        return render(request,'Yorking/user_team.html',{'batsmen':batsmen_selected,'bowler':bowler_selected,'all_rounder':all_rounder_selected,'wicket_keeper':wicket_keeper_selected})


def dashboard(request):
    # captain_id = request.POST["captain"]
    # match_id_obj = match_user.objects.get(match_id = request.session['matchid'])
    # user_id_obj=user.objects.get(user_id__exact=''''''')
    # print(user_id_obj)
    # user_team_obj = user_team(user_id =user_id_obj ,match_id = match_id_obj,captain = captain_id)
    # user_team_obj.save()
    # user_match = user_team.objects.get(match_id = request.session['matchid'],user_id = 3)
    # for i in request.session['selected_players']:
    #     pid = country_team.objects.get(player_id = i)
    #     cp = choosen_players(user_match = user_match,player_id= pid )
    #     cp.save()
    return HttpResponse("<h1> Congrats :) </h1>")



@csrf_exempt
def get_points(request):
	p_id = request.POST["id"]
	global points
	print("pid",p_id)
	print("points",points)
	p_points = country_team.objects.filter(player_id=p_id)
	if(int(request.POST["checked"])):
		new_points = int(points) - int(p_points[0].points)
		points = new_points
	else:
		new_points = int(points) + int(p_points[0].points)
		points = new_points

	return HttpResponse(new_points)
