from django.contrib import admin
from .models import CreateGroupOfTasks, Createtask, CreateList


admin.site.site_header = 'Toodoo admin'




class ListInline(admin.TabularInline):
    model = CreateList
    extra = 3


class GroupOfLists(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['title']}),
                 ("Date information", {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ListInline]


class TaskInline(admin.TabularInline):
    model = Createtask
    extra = 3

class GroupOfTasks(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['title']}),
                 ("Date information", {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [TaskInline]


admin.site.register(CreateGroupOfTasks, GroupOfLists)
admin.site.register(CreateList, GroupOfTasks)
