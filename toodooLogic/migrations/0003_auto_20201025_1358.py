# Generated by Django 3.1.2 on 2020-10-25 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toodooLogic', '0002_auto_20201025_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='createlist',
            name='whichGroup',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='toodooLogic.creategroupoftasks'),
        ),
        migrations.AddField(
            model_name='createtask',
            name='whichList',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='toodooLogic.createlist'),
        ),
        migrations.AlterField(
            model_name='creategroupoftasks',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='createlist',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, verbose_name='date published'),
        ),
    ]
