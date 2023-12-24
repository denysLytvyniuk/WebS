# Generated by Django 4.2.2 on 2023-12-24 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chessgame',
            name='id',
        ),
        migrations.AddField(
            model_name='chessgame',
            name='game_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='chessgame',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='chessgame',
            name='winner',
            field=models.CharField(blank=True, default='Undecided', max_length=100, null=True),
        ),
    ]
