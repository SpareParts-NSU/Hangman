# Generated by Django 2.1.5 on 2019-04-28 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Server', '0015_remove_match_gameid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game_data',
            name='gameID',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]
