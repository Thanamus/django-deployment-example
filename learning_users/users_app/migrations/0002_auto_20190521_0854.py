# Generated by Django 2.1.7 on 2019-05-21 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='portfolio_pic',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pic'),
        ),
    ]