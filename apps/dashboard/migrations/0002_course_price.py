# Generated by Django 2.2 on 2020-05-28 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]