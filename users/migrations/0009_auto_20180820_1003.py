# Generated by Django 2.1 on 2018-08-20 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20180820_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driverdata',
            name='bus_no',
        ),
        migrations.RemoveField(
            model_name='driverdata',
            name='bus_reg_no',
        ),
        migrations.RemoveField(
            model_name='driverdata',
            name='license_no',
        ),
        migrations.AddField(
            model_name='driverdata',
            name='address',
            field=models.CharField(blank=True, help_text='enter the address', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='driverdata',
            name='email',
            field=models.EmailField(blank=True, help_text='enter the email', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='driverdata',
            name='first_name',
            field=models.CharField(blank=True, help_text='enter the first name of user', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='driverdata',
            name='last_name',
            field=models.CharField(blank=True, help_text='enter the last name', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='driverdata',
            name='password',
            field=models.CharField(blank=True, help_text='enter the strong password', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='driverdata',
            name='username',
            field=models.CharField(blank=True, help_text='enter the username', max_length=100, null=True),
        ),
    ]
