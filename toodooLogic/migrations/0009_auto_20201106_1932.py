# Generated by Django 3.1.2 on 2020-11-06 16:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toodooLogic', '0008_auto_20201106_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creategroupoftasks',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 6, 19, 32, 26, 438061), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='createlist',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 6, 19, 32, 26, 439060), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='createtask',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 6, 19, 32, 26, 439060), verbose_name='date published'),
        ),
    ]
