# Generated by Django 4.2.11 on 2024-03-15 11:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_employee_created_at_employee_exited_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='created_at',
        ),
        migrations.AddField(
            model_name='employee',
            name='entered_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 15, 11, 23, 20, 111099, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]