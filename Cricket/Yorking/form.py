from django import forms
from django.core import validators
from Yorking.models import user

class User_Authentication(forms.Form):
    user_obj=user.objects.all().values()
    user_name=forms.CharField(max_length=100)
    email = forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput,validators=[validators.MinLengthValidator(5)])


    def clean(self):
        all_clean_data = super().clean()
        user_name=all_clean_data['user_name']
        user_obj=all_clean_data['user_obj']
        for i in user_obj:
            if user_name==i['user_name']:
                raise forms.ValidationError('Username already exists. Please choose an other one')











    # match_user_obj=match_user.objects.filter(status__exact='Not occured').values('match_id')
    # listof=[]
    # for i in match_user_obj:
    #     listof.append((i,i))
    # matchid=forms.UUIDField(widget=forms.RadioSelect(choices=listof))
