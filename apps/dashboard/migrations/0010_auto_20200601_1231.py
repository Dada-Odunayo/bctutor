# Generated by Django 2.2 on 2020-06-01 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0009_auto_20200601_1224'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fb_link', models.TextField(blank=True, max_length=500)),
                ('dp', models.ImageField(blank=True, upload_to='dp')),
                ('phone_number', models.CharField(blank=True, max_length=12)),
                ('specialize', models.TextField(blank=True, max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Userdetail',
        ),
    ]
