# Generated by Django 5.0.4 on 2024-05-05 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserModule', '0003_usermodel_isteacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='profile_image',
            field=models.IntegerField(default=1, verbose_name='عکس پروفایل'),
        ),
    ]
