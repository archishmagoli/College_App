# Generated by Django 3.2.3 on 2021-06-06 19:05

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycolleges', '0004_college_user'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='college',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]