# Generated by Django 3.1.4 on 2021-07-29 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
