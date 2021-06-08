# Generated by Django 3.2.3 on 2021-06-08 00:13

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
            name='JournalEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('mood', models.CharField(blank=True, choices=[('cry.jpg', 'Terrible'), ('sad.jpg', 'Could be better'), ('neutral.jpg', 'Alright'), ('slight.jpg', 'Good'), ('big.jpg', 'Great')], max_length=30, null=True)),
                ('journal', models.TextField(max_length=500)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
