# Generated by Django 2.1 on 2018-08-18 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180818_1221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driverdata',
            old_name='driver_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='driverdata',
            old_name='license_no',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='driverdata',
            old_name='institution_bus_no',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='driverdata',
            name='registration_no',
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
            name='password',
            field=models.CharField(blank=True, help_text='enter the strong password', max_length=100, null=True),
        ),
    ]
