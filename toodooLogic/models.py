from django.db import models
import datetime


class CreateGroupOfTasks(models.Model):
    title = models.CharField(max_length=40, db_index=True)
    pub_date = models.DateTimeField('date published',
                                    default=datetime.datetime.now())

    def __str__(self):
        return self.title


class CreateList(models.Model):
    whichGroup = models.ForeignKey(CreateGroupOfTasks, null=True,
                                   on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    pub_date = models.DateTimeField('date published', default=datetime.datetime.now())

    def __str__(self):
        return self.title


class Createtask(models.Model):
    whichList = models.ForeignKey(CreateList,
                                   on_delete=models.CASCADE, null=True)
    titleTask = models.CharField(max_length=40)
    pub_date = models.DateTimeField('date published', default=datetime.datetime.now())


    def __str__(self):
        return self.titleTask
