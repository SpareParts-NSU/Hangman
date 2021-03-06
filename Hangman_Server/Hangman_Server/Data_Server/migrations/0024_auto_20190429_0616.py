# Generated by Django 2.1.5 on 2019-04-29 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Server', '0023_auto_20190429_0502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leader_Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Days', models.IntegerField(blank=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Data_Server.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='match',
            name='Winner',
        ),
        migrations.AddField(
            model_name='game_data',
            name='Winner',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='Winner', to='Data_Server.User'),
        ),
    ]
