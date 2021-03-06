# Generated by Django 2.1 on 2018-08-13 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, help_text='enter the first name of user', max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, help_text='enter the last name', max_length=100, null=True)),
                ('address', models.CharField(blank=True, help_text='enter the address', max_length=300, null=True)),
                ('contact', models.CharField(blank=True, help_text='enter the contact', max_length=100, null=True)),
                ('email', models.EmailField(blank=True, help_text='enter the email', max_length=100, null=True)),
                ('username', models.CharField(blank=True, help_text='enter the username', max_length=100, null=True)),
                ('password', models.CharField(blank=True, help_text='enter the strong password', max_length=100, null=True)),
                ('creation_date', models.DateTimeField(editable=False, null=True)),
                ('last_modified', models.DateTimeField(editable=False, null=True)),
                ('author', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
