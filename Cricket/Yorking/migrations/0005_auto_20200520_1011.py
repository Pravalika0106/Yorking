# Generated by Django 3.0.6 on 2020-05-20 04:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Yorking', '0004_auto_20200520_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country_team',
            name='player_id',
            field=models.UUIDField(default=uuid.UUID('d242e9a5-3af6-40f8-9e65-17ba6312ee9a'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='match_user',
            name='match_id',
            field=models.UUIDField(default=uuid.UUID('a9457ff9-e37a-4a64-9929-7058cbd94bb0'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.UUIDField(default=uuid.UUID('a8f2a611-f59c-4a39-a86e-68d8dee905d3'), editable=False, primary_key=True, serialize=False),
        ),
    ]
