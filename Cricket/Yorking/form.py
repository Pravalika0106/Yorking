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
        flag1=0
        flag2=0
        print(user_id)
        print(len(user_id))
        print(password)
        for i in user_obj:
            if i['user_id']==user_id:
                flag=1
                print(user_id)
                print(len(user_id))
                print(flag1)
        if flag1!=1:
                raise forms.ValidationError('Please check your User Id')
            # if password==i['password']:
            #     flag2=1
            #     print(password)
            #     print(flag2)
            #     if flag2!=1:
            #         raise forms.ValidationError('Please check your Password')
