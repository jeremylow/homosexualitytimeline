# Generated by Django 2.0.2 on 2018-04-08 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maintimeline', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
