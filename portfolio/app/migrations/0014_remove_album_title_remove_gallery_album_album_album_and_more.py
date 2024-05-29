# Generated by Django 5.0 on 2024-05-27 05:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_testimonial_client_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='title',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='album',
        ),
        migrations.AddField(
            model_name='album',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hostings', to='app.gallery'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.FileField(upload_to='Galleryimage'),
        ),
    ]