# Generated by Django 2.1.5 on 2019-04-27 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Server', '0004_auto_20190427_0636'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(default=None, max_length=8)),
                ('seed', models.IntegerField(blank=True)),
                ('Player_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Player_1', to='Data_Server.User')),
                ('Player_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Player_2', to='Data_Server.User')),
                ('Winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Winner', to='Data_Server.User')),
            ],
        ),
        migrations.RenameField(
            model_name='achievement',
            old_name='alias',
            new_name='Player',
        ),
        migrations.RenameField(
            model_name='achievement',
            old_name='achivement',
            new_name='achievement',
        ),
    ]
