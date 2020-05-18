from django import forms
from django.core import validators
from Yorking.models import match_user

class MatchesForm(forms.Form):
    match_user_obj=match_user.objects.filter(status__exact='Not occured').values('match_id')
    listof=[]
    for i in match_user_obj:
        listof.append((i,i))
    matchid=forms.UUIDField(widget=forms.RadioSelect(choices=listof))
