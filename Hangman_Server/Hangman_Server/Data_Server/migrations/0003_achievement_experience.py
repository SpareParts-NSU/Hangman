# Generated by Django 2.1.5 on 2019-04-27 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Server', '0002_auto_20190426_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='experience',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
