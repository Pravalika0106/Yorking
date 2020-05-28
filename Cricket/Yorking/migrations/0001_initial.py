# Generated by Django 3.0.6 on 2020-05-28 06:07

import Yorking.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='country_team',
            fields=[
                ('player_id', models.CharField(default=Yorking.models.uuid_hex, editable=False, max_length=100, primary_key=True, serialize=False)),
                ('player_name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('points', models.IntegerField(default=6)),
                ('country', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='match_user',
            fields=[
                ('match_id', models.CharField(default=Yorking.models.uuid_hex, editable=False, max_length=100, primary_key=True, serialize=False)),
                ('country1', models.CharField(max_length=200)),
                ('country2', models.CharField(max_length=200)),
                ('status', models.CharField(default='Not occured', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('user_name', models.CharField(editable=False, max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='user_team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('captain', models.CharField(default='Not Decided', max_length=200)),
                ('stars', models.IntegerField(default=0)),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Yorking.match_user')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Yorking.user')),
            ],
            options={
                'unique_together': {('user_name', 'match_id')},
            },
        ),
        migrations.CreateModel(
            name='match_performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('runs', models.IntegerField(default=0)),
                ('catches', models.IntegerField(default=0)),
                ('wickets', models.IntegerField(default=0)),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Yorking.match_user')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Yorking.country_team')),
            ],
            options={
                'unique_together': {('match_id', 'player_id')},
            },
        ),
        migrations.CreateModel(
            name='choosen_players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Yorking.country_team')),
                ('user_match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Yorking.user_team')),
            ],
            options={
                'unique_together': {('user_match', 'player_id')},
            },
        ),
    ]
