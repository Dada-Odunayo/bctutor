# Generated by Django 2.2 on 2020-06-01 10:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0003_userdetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Userdetails',
            new_name='Userdetail',
        ),
    ]
