# Generated by Django 3.0.6 on 2020-05-19 18:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Yorking', '0003_auto_20200519_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country_team',
            name='player_id',
            field=models.UUIDField(default=uuid.UUID('6e8c29a9-93de-4315-a56d-bf62a58f77ca'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='match_user',
            name='match_id',
            field=models.UUIDField(default=uuid.UUID('5560c98e-73cf-4b73-8dd2-293c68fde53f'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.UUIDField(default=uuid.UUID('48498c80-368d-46d4-88e2-789e518c2054'), editable=False, primary_key=True, serialize=False),
        ),
    ]