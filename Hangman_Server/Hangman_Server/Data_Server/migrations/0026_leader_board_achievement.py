# Generated by Django 2.1.5 on 2019-04-29 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Server', '0025_auto_20190429_0616'),
    ]

    operations = [
        migrations.AddField(
            model_name='leader_board',
            name='achievement',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Player_1', to='Data_Server.Achievement'),
        ),
    ]