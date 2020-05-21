import os
from uuid import uuid4
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Cricket.settings')

import django
django.setup()

import random
from Yorking.models import country_team,user_team,choosen_players,match_user,user,match_performance
from faker import Faker

fakegen = Faker()
#ACTUAL COUNTRIES
# countries=['Australia','England','South Africa','West Indies','New Zealand','India,Pakistan','Sri Lanka','Zimbabwe',
#             'Bangladesh','Afghanistan','Ireland','Argentina','Belgium','Bermuda','Botswana','Canada','Cayman Islands',
#             'Denmark','Fiji','France','Germany','Gibraltar','Guernsey','Hong Kong','Israel','Italy','Japan','Jersey','Kenya',
#             'Kuwait','Malaysia','Namibia','Nepal','Netherlands','Nigeria','Oman','Papua New Guinea','Scotland','Singapore',
#             'Suriname','Tanzania','Thailand','Uganda','United Arab Emirates','USA','Vanuatu','Zambia']

countries=['Australia','England','South Africa','West Indies','New Zealand','India','Pakistan']
# 'Sri Lanka','Zimbabwe','Bangladesh'

categories=['batsman','baller','wicketkeeper','allrounder']
def populate(N=5):
    for entry in range(N):
        player_id=uuid4()
        player_name=fakegen.name_male()
        category=random.choice(categories)
        points=random.randrange(1,13)
        country=random.choice(countries)

        user_id=uuid4()
        user_name=fakegen.name()
        phn_num=fakegen.msisdn()
        email=fakegen.email()
        password=user_name+'1234'

        match_id=uuid4()

        runs=random.randrange(0,150)
        catches=random.randrange(0,9)
        wickets=random.randrange(0,9)

        count_team=country_team.objects.get_or_create(player_id=player_id,player_name=player_name,category=category,points=points,country=country)[0]

        # user_obj=user.objects.get_or_create(user_id=user_id,user_name=user_name,phn_num=phn_num,email=email,password=password)[0]

        # match_user_obj=match_user.objects.get_or_create(match_id=match_id)[0]

        # match_performance_obj=match_performance.objects.get_or_create(match_id=match_user_obj,player_id=count_team,runs=runs,catches=catches,wickets=wickets)[0]

        # user_team_obj=user_team.objects.get_or_create(user_id=user_obj,match_id=match_user_obj,captain='Not Decided')[0]



if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(10)
    print('Populating Complete')
