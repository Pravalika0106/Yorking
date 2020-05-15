from django.contrib import admin
from Yorking.models import country_team,user_team,choosen_players, match_user,user,match_performance
# Register your models here.

admin.site.register(country_team)
admin.site.register(user_team)
admin.site.register(choosen_players)
admin.site.register(match_user)
admin.site.register(user)
admin.site.register(match_performance)
