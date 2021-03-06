# Generated by Django 2.1.5 on 2019-04-29 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Server', '0021_remove_game_data_gameid'),
    ]

    operations = [
        migrations.AddField(
            model_name='game_data',
            name='gameStart',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game_data',
            name='hit_p1',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='game_data',
            name='hit_p2',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
