# Generated by Django 3.0.6 on 2020-05-20 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Yorking', '0007_auto_20200520_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country_team',
            name='player_id',
            field=models.CharField(default='e2e5386f881f442c8c1ce85957e955e4', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='match_user',
            name='match_id',
            field=models.CharField(default='e7ba624b591c4bc59bfff1af184d9035', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(default='3115eea1b28c4e02a8f3fb7a3d998706', max_length=100, primary_key=True, serialize=False),
        ),
    ]