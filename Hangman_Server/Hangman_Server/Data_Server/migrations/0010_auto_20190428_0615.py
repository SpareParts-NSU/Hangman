# Generated by Django 2.1.5 on 2019-04-28 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Server', '0009_auto_20190428_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='gameID',
            field=models.IntegerField(blank=True),
        ),
    ]
