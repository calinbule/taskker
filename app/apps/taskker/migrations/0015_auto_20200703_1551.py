# Generated by Django 3.0.7 on 2020-07-03 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskker', '0014_auto_20200703_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priority',
            name='name',
            field=models.CharField(choices=[('p1', 'p1'), ('p2', 'p2'), ('p3', 'p3'), ('no_priority', 'no')], max_length=255),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.ForeignKey(blank=True, default='no_priority', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='taskker.Priority'),
        ),
    ]
