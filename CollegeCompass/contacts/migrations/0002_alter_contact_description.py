# Generated by Django 3.2.3 on 2021-06-06 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]