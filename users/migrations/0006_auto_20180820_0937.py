# Generated by Django 2.1 on 2018-08-20 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20180818_1306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driverdata',
            old_name='license_no',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='driverdata',
            name='bus_no',
        ),
        migrations.RemoveField(
            model_name='driverdata',
            name='bus_reg_no',
        ),
    ]
