# Generated by Django 5.0 on 2024-05-28 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_remove_herobanner_completedproject_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Albumimage'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='galleryimage'),
        ),
    ]
