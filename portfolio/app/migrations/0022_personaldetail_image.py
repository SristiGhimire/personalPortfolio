# Generated by Django 5.0 on 2024-05-27 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_personaldetail_companyname'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldetail',
            name='image',
            field=models.FileField(default=1, upload_to='smallImage'),
            preserve_default=False,
        ),
    ]
