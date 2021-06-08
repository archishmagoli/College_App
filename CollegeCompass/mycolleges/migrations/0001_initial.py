# Generated by Django 3.2.3 on 2021-06-05 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('1', 'Safety'), ('2', 'Match'), ('3', 'Reach')], max_length=50)),
                ('description', models.CharField(blank=True, default='', max_length=500)),
            ],
        ),
    ]