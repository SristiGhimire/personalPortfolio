# Generated by Django 5.0 on 2024-05-27 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_personaldetail_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='herobanner',
            name='completedProject',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='herobanner',
            name='satisfiedClient',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
    ]
