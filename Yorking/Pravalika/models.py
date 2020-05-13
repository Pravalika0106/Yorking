from django.db import models

# Create your models here.

class country_team(models.Model):
	player_id=models.IntegerField(primary_key=True)
	player_name=models.CharField(max_length=200)
	category=models.CharField(max_length=200)
	points=models.IntegerField(default=6)
	country=models.CharField(max_length=200)

class user_team(models.Model):
	user_id=models.ForeignKey('user',on_delete=models.CASCADE)
	match_id=models.ForeignKey('match_user',on_delete=models.CASCADE)
	captain=models.IntegerField(default=0)
	class Meta:
		unique_together=(('user_id','match_id'),)

class choosen_players(models.Model):
	user_match=models.ForeignKey('user_team',on_delete=models.CASCADE)
	player_id=models.ForeignKey('country_team',on_delete=models.CASCADE)


class match_user(models.Model):
	match_id=models.IntegerField(primary_key=True)
	country1=models.CharField(max_length=200)
	country2=models.CharField(max_length=200)
	status=models.CharField(max_length=200)

class user(models.Model):
	user_id=models.IntegerField(primary_key=True)
	user_name=models.CharField(max_length=200)
	phn_num=models.IntegerField(default=None)
	email=models.CharField(max_length=200)
	password=models.CharField(max_length=200)

class match_performance(models.Model):
	match_id=models.CharField(max_length=200)
	player_id=models.CharField(max_length=200)
	runs=models.IntegerField(default=0)
	catches=models.IntegerField(default=0)
	wickets=models.IntegerField(default=0)
	category=models.CharField(max_length=200,default="all rounder")
