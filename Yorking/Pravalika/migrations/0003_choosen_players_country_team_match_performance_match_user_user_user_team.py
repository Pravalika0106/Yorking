# Generated by Django 3.0.6 on 2020-05-11 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Pravalika', '0002_auto_20200511_1929'),
    ]

    operations = [
        migrations.CreateModel(
            name='country_team',
            fields=[
                ('player_id', models.IntegerField(primary_key=True, serialize=False)),
                ('player_name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('points', models.IntegerField(default=6)),
                ('country', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='match_user',
            fields=[
                ('match_id', models.IntegerField(primary_key=True, serialize=False)),
                ('country1', models.CharField(max_length=200)),
                ('country2', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=200)),
                ('phn_num', models.IntegerField(default=None)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='user_team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('captain', models.IntegerField(default=0)),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pravalika.match_user')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pravalika.user')),
            ],
            options={
                'unique_together': {('user_id', 'match_id')},
            },
        ),
        migrations.CreateModel(
            name='choosen_players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pravalika.country_team')),
                ('user_match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pravalika.user_team')),
            ],
        ),
        migrations.CreateModel(
            name='match_performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('runs', models.IntegerField(default=0)),
                ('catches', models.IntegerField(default=0)),
                ('wickets', models.IntegerField(default=0)),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pravalika.match_user')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pravalika.country_team')),
            ],
            options={
                'unique_together': {('match_id', 'player_id')},
            },
        ),
    ]
