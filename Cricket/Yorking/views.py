from django.shortcuts import render
from Yorking.models import match_user,country_team,match_performance
from Yorking import form
from uuid import uuid4
# Create your views here.
def index(request):
    return render(request,'Yorking/index.html')

def edit_selection(request):
    match_user_obj=match_user.objects.filter(status__exact='Not occured')
    return render(request,'Yorking/edit_selection.html',{'matchcountries':match_user_obj})

def playerperfomance(request):
    if request.method=='POST':
        matchid=request.POST.get('matchid')
        request.session['matchid']=matchid
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
    print(batsman1)
    print(baller1)
    print('above is batsman and baller 1')
    batsmanone=request.POST.getlist('batsman1')
    ballerone=request.POST.getlist('baller1')
    wicketkeeperone=request.POST.getlist('wicketkeeper1')
    allrounderone=request.POST.getlist('allrounder1')
    batsmantwo=request.POST.getlist('batsman2')
    ballertwo=request.POST.getlist('baller2')
    wicketkeepertwo=request.POST.getlist('wicketkeeper2')
    allroundertwo=request.POST.getlist('allrounder2')
    print(batsmanone)
    print(ballerone)
    validation=[]
    if len(batsmanone)<1:
        validation.append("Min 4 batsman required in Country 1")
    if len(ballerone)<1:
        validation.append("Min 3 ballers required in Country 1")
    if len(wicketkeeperone)<1:
        validation.append("Min 1 wicketkeeper required you got 0 in Country 1")
    if len(allrounderone)<1:
        validation.append("Min 1 allrounder required you got 0 in Country 1")
    if len(batsmanone)+len(ballerone)+len(wicketkeeperone)+len(allrounderone)<4:
        validation.append("Min 11 players required in Country 1")
    if len(batsmantwo)<1:
        validation.append("Min 4 batsman required in Country 2")
    if len(ballertwo)<1:
        validation.append("Min 3 ballers required in Country 2")
    if len(wicketkeepertwo)<1:
        validation.append("Min 1 wicketkeeper required you got 0 in Country 2")
    if len(allroundertwo)<1:
        validation.append("Min 1 allrounder required you got 0 in Country 2")
    if len(batsmantwo)+len(ballertwo)+len(wicketkeepertwo)+len(allroundertwo)<4:
        validation.append("Min 11 players required in Country 2")
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
    # batsmanone=request.POST.getlist('batsman1')
    # ballerone=request.POST.getlist('baller1')
    # wicketkeeperone=request.POST.getlist('wicketkeeper1')
    # allrounderone=request.POST.getlist('allrounder1')
    # batsmantwo=request.POST.getlist('batsman2')
    # ballertwo=request.POST.getlist('baller2')
    # wicketkeepertwo=request.POST.getlist('wicketkeeper2')
    # allroundertwo=request.POST.getlist('allrounder2')

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
    matchid=request.session['matchid']
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
    # match_user_obj=match_user.objects.get(match_id__exact=matchid)
    # match_user_obj.status='Available'
    # match_user_obj.save()
    match_user_obj.objects.filter(match_id__exact=matchid).update(status='Available')
    return render(request,'Yorking/index.html')




#
# def djangoform(request):
#     form_obj=form.MatchesForm(request.POST)
#     if request.method=='POST' and form_obj.is_valid():
#         print(form_obj.cleaned_data.get('matchid'))
#     else:
#         print('form is not valid')
#     return render(request,'Yorking/djangoform.html',{'form':form_obj})

def modelform(request):
    country_team_obj=country_team.objects.order_by('country').values('country').distinct()
    return render(request,'Yorking/form.html',{'error':[],'countries':country_team_obj})

def uuid_hex():
	return uuid4().hex

def form_check(request):
    coun1=request.POST.get('country1')
    coun2=request.POST.get('country2')
    error=[]
    if coun1 == coun2:
        error.append('Select two different countries')
        country_team_obj=country_team.objects.order_by('country').values('country').distinct()
        return render(request,'Yorking/form.html',{'error':error,'countries':country_team_obj})
    else:
        # match_id_created=uuid4().hex
        match_id_created=uuid_hex
        #USED IN PERFOMANCE_ONE_SAVE
        request.session['match_id_created']=match_id_created
        matchuserobj=match_user(match_id=match_id_created,country1=coun1,country2=coun2)
        matchuserobj.save()

        #POSTED FROM FORM.HTML
        select=request.POST.get('select')
        submit=request.POST.get('submit')

        if select == '':
            batsman_1=country_team.objects.filter(country__exact=coun1,category__exact='batsman').values()
            #THE SESSIONS HERE ARE TO USE THE DATA IN CHECK_CONSTRAINS_ONE
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

        #POSTED FROM FORM.HTML
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
    print(batsman_one)
    print('selected batsman')
    validation=[]
    if len(batsman_one)<1:
        validation.append("Min 4 batsman required in Country 1")
    if len(baller_one)<1:
        validation.append("Min 3 ballers required in Country 1")
    if len(wicketkeeper_one)<1:
        validation.append("Min 1 wicketkeeper required you got 0 in Country 1")
    if len(allrounder_one)<1:
        validation.append("Min 1 allrounder required you got 0 in Country 1")
    if len(batsman_one)+len(baller_one)+len(wicketkeeper_one)+len(allrounder_one)<4:
        validation.append("Min 11 players required in Country 1")
    if len(batsman_two)<1:
        validation.append("Min 4 batsman required in Country 2")
    if len(baller_two)<1:
        validation.append("Min 3 ballers required in Country 2")
    if len(wicketkeeper_two)<1:
        validation.append("Min 1 wicketkeeper required you got 0 in Country 2")
    if len(allrounder_two)<1:
        validation.append("Min 1 allrounder required you got 0 in Country 2")
    if len(batsman_two)+len(baller_two)+len(wicketkeeper_two)+len(allrounder_two)<4:
        validation.append("Min 11 players required in Country 2")
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
        print(batsman_one_selected)
        print('this is batsman_one with id')
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
        # match_user_obj=match_user.objects.get(match_id__exact=matchid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,runs=runs)
        match_performance_obj.save()
    for i in baller_one_selected:
        playerid=i['player_id']
        catches=request.POST.get(playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        # match_user_obj=match_user.objects.get(match_id__exact=matchid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,catches=catches)
        match_performance_obj.save()
    for i in wicketkeeper_one_selected:
        playerid=i['player_id']
        wickets=request.POST.get(playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        # match_user_obj=match_user.objects.get(match_id__exact=matchid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,wickets=wickets)
        match_performance_obj.save()
    for i in allrounder_one_selected:
        playerid=i['player_id']
        runs=request.POST.get('runs'+playerid)
        catches=request.POST.get('catches'+playerid)
        wickets=request.POST.get('wickets'+playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        # match_user_obj=match_user.objects.get(match_id__exact=matchid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,runs=runs,catches=catches,wickets=wickets)
        match_performance_obj.save()

    for i in batsman_two_selected:
        playerid=i['player_id']
        runs=request.POST.get(playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        # match_user_obj=match_user.objects.get(match_id__exact=matchid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,runs=runs)
        match_performance_obj.save()
    for i in baller_two_selected:
        playerid=i['player_id']
        catches=request.POST.get(playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        # match_user_obj=match_user.objects.get(match_id__exact=matchid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,catches=catches)
        match_performance_obj.save()
    for i in wicketkeeper_two_selected:
        playerid=i['player_id']
        wickets=request.POST.get(playerid)
        # match_user_obj=match_user.objects.get(match_id__exact=matchid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,wickets=wickets)
        match_performance_obj.save()
    for i in allrounder_two_selected:
        playerid=i['player_id']
        runs=request.POST.get('runs'+playerid)
        catches=request.POST.get('catches'+playerid)
        wickets=request.POST.get('wickets'+playerid)
        country_team_obj=country_team.objects.get(player_id__exact=playerid)
        # match_user_obj=match_user.objects.get(match_id__exact=matchid)
        match_performance_obj=match_performance(match_id=match_user_obj,player_id=country_team_obj,runs=runs,catches=catches,wickets=wickets)
        match_performance_obj.save()
    # match_user_obj=match_user.objects.get(match_id__exact=match_id_created)
    # match_user_obj.status='Available'
    # match_user_obj.save()
    # return render(request,'Yorking/index.html')
    match_user_obj.objects.filter(match_id__exact=match_id_created).update(status='Available')
