# Generated by Django 2.1 on 2018-08-20 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20180820_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='author',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
