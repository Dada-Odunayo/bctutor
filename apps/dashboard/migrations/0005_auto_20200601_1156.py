# Generated by Django 2.2 on 2020-06-01 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20200601_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='dp',
            field=models.ImageField(upload_to='profilepic'),
        ),
    ]
