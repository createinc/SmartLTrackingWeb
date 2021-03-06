# Generated by Django 2.1 on 2018-08-20 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20180820_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='notapro',
            name='address',
            field=models.CharField(blank=True, help_text='enter the address', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='notapro',
            name='email',
            field=models.EmailField(blank=True, help_text='enter the email', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='notapro',
            name='first_name',
            field=models.CharField(blank=True, help_text='enter the first name of user', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='notapro',
            name='last_name',
            field=models.CharField(blank=True, help_text='enter the last name', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='notapro',
            name='password',
            field=models.CharField(blank=True, help_text='enter the strong password', max_length=100, null=True),
        ),
    ]
