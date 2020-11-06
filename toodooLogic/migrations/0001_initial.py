# Generated by Django 3.1.2 on 2020-11-02 05:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateGroupOfTasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=40)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2020, 11, 2, 8, 55, 38, 60411), verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='CreateList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2020, 11, 2, 8, 55, 38, 60411), verbose_name='date published')),
                ('whichGroup', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='toodooLogic.creategroupoftasks')),
            ],
        ),
        migrations.CreateModel(
            name='Createtask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2020, 11, 2, 8, 55, 38, 61408), verbose_name='date published')),
                ('whichList', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='toodooLogic.createlist')),
            ],
        ),
    ]
