# Generated by Django 3.0.6 on 2020-05-12 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pravalika', '0004_auto_20200512_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='match_performance',
            name='category',
            field=models.CharField(default='all rounder', max_length=200),
        ),
    ]
