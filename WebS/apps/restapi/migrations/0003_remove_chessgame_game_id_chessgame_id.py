# Generated by Django 4.2.2 on 2023-12-24 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0002_remove_chessgame_id_chessgame_game_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chessgame',
            name='game_id',
        ),
        migrations.AddField(
            model_name='chessgame',
            name='id',
            field=models.BigAutoField(auto_created=True, default=2, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
