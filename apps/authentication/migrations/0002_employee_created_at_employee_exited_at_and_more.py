# Generated by Django 4.2.11 on 2024-03-15 02:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='exited_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 15, 2, 40, 30, 818026)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='vacation_days',
            field=models.IntegerField(default=0),
        ),
    ]
