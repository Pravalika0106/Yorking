from django import forms
from django.core import validators
from Yorking.models import user

class User_Authentication(forms.Form):
    user_obj=user.objects.all().values()
    user_id=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput,validators=[validators.MinLengthValidator(5)])


    def clean(self):
        all_clean_data = super().clean()
        user_obj=user.objects.all().values()
        user_id=all_clean_data['user_id']
        password=all_clean_data['password']
        # user_obj=all_clean_data['user_obj']
        for i in user_obj:
            if user_id!=i['user_id']:
                raise forms.ValidationError('Enter the correct user id')
            if password!=i['password']:
                raise forms.ValidationError('Enter the correct password')











    # match_user_obj=match_user.objects.filter(status__exact='Not occured').values('match_id')
    # listof=[]
    # for i in match_user_obj:
    #     listof.append((i,i))
    # matchid=forms.UUIDField(widget=forms.RadioSelect(choices=listof))
