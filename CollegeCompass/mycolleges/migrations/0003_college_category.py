# Generated by Django 3.2.3 on 2021-06-05 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycolleges', '0002_auto_20210605_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='category',
            field=models.CharField(blank=True, choices=[('Safety', 'Safety'), ('Match', 'Match'), ('Reach', 'Reach')], max_length=30, null=True),
        ),
    ]
