# Generated by Django 2.1.5 on 2019-04-28 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Server', '0010_auto_20190428_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game_data',
            name='gameID',
            field=models.IntegerField(blank=True),
        ),
    ]
