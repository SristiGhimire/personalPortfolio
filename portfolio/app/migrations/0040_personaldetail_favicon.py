# Generated by Django 5.0 on 2024-05-29 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_personaldetail_mapurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldetail',
            name='favicon',
            field=models.FileField(default=1, upload_to='Favicon'),
            preserve_default=False,
        ),
    ]
