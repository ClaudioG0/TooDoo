# Generated by Django 3.1.2 on 2020-10-25 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toodooLogic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createlist',
            name='whichGroup',
        ),
        migrations.RemoveField(
            model_name='createtask',
            name='whichList',
        ),
    ]
