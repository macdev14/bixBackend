# Generated by Django 4.2.11 on 2024-03-15 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_employee_entered_at_alter_employee_exited_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='entered_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]