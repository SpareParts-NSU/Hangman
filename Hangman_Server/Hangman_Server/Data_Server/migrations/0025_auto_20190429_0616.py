# Generated by Django 2.1.5 on 2019-04-29 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Server', '0024_auto_20190429_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game_data',
            name='Winner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Winner', to='Data_Server.User'),
        ),
    ]
