# Generated by Django 5.0 on 2024-05-26 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_appointment_buttonname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='buttonName',
        ),
    ]
