# Generated by Django 2.1.5 on 2019-04-28 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Server', '0011_auto_20190428_0618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='gameID',
        ),
    ]
