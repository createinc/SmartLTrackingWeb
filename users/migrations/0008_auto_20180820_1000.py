# Generated by Django 2.1 on 2018-08-20 10:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0007_auto_20180820_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, help_text='enter the first name of user', max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, help_text='enter the last name', max_length=100, null=True)),
                ('address', models.CharField(blank=True, help_text='enter the address', max_length=300, null=True)),
                ('contact', models.IntegerField(blank=True, help_text='enter the contact', null=True)),
                ('email', models.EmailField(blank=True, help_text='enter the email', max_length=100, null=True)),
                ('username', models.CharField(blank=True, help_text='enter the username', max_length=100, null=True)),
                ('password', models.CharField(blank=True, help_text='enter the strong password', max_length=100, null=True)),
                ('creation_date', models.DateTimeField(editable=False, null=True)),
                ('last_modified', models.DateTimeField(editable=False, null=True)),
                ('author', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='driverdata',
            name='address',
        ),
        migrations.AddField(
            model_name='driverdata',
            name='bus_no',
            field=models.CharField(blank=True, help_text='enter the bus number', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='driverdata',
            name='bus_reg_no',
            field=models.CharField(blank=True, help_text='enter the bus register number', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='driverdata',
            name='license_no',
            field=models.CharField(blank=True, help_text='enter the license number', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='driverdata',
            name='username',
            field=models.CharField(blank=True, help_text='enter the bus driver name', max_length=100, null=True),
        ),
    ]
