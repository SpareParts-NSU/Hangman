# Generated by Django 2.1.5 on 2019-04-28 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Server', '0017_game_data_word'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game_data',
            name='gameID',
        ),
    ]
