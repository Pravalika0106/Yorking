from django.db import models
from uuid import uuid4
from django.core.exceptions import ValidationError
# Create your models here.

def uuid_hex():
	return uuid4().hex

class country_team(models.Model):
	player_id=models.CharField(primary_key=True,default=uuid_hex,max_length=100,editable=False)
	player_name=models.CharField(max_length=200)
	category=models.CharField(max_length=200)
	points=models.IntegerField(default=6)
	country=models.CharField(max_length=200)

class user(models.Model):
	user_name=models.CharField(primary_key=True,max_length=100,editable=False)
	password=models.CharField(max_length=200)
	user_mail=models.EmailField(max_length=100)

class match_user(models.Model):
    match_id=models.CharField(primary_key=True,default=uuid_hex,max_length=100,editable=False)
    country1=models.CharField(max_length=200)
    country2=models.CharField(max_length=200)
    status=models.CharField(max_length=200,default='Not occured')

class match_performance(models.Model):
	match_id=models.ForeignKey('match_user',on_delete=models.CASCADE)
	player_id=models.ForeignKey('country_team',on_delete=models.CASCADE)
	runs=models.IntegerField(default=0)
	catches=models.IntegerField(default=0)
	wickets=models.IntegerField(default=0)
	class Meta:
		unique_together = (('match_id', 'player_id'),)

class user_team(models.Model):
	user_id=models.ForeignKey('user',on_delete=models.CASCADE)
	match_id=models.ForeignKey('match_user',on_delete=models.CASCADE)
	captain=models.CharField(max_length=200,default='Not Decided')
	stars=models.IntegerField(default=0)
	class Meta:
		unique_together=(('user_id','match_id'),)

class choosen_players(models.Model):
	user_match=models.ForeignKey('user_team',on_delete=models.CASCADE)
	player_id=models.ForeignKey('country_team',on_delete=models.CASCADE)
	class Meta:
		unique_together=(('user_match','player_id'),)
