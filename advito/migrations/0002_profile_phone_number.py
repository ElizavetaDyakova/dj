# Generated by Django 3.1.1 on 2020-09-15 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advito', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(default=None, max_length=12),
        ),
    ]