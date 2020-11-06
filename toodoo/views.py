from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from toodooLogic.forms import AddListForm, AddGroupForm, AddItemForm
from toodooLogic.models import Createtask, CreateGroupOfTasks, CreateList

@login_required
def index(request):
    tasks = Createtask.objects.all()



    if request.method == 'POST':
        if 'addlist' in request.POST:
            form1 = AddListForm(request.POST)
            if form1.is_valid():
                form1.save()

        elif 'addgroup' in request.POST:
            form2 = AddGroupForm(request.POST)
            if form2.is_valid():
                form2.save()

        elif 'additem' in request.POST:
            form3 = AddItemForm(request.POST or None)
            if form3.is_valid():
                form3.save()
        return redirect('/')

    context = {
        'listForm': AddListForm,
        'groupForm': AddGroupForm,
        'itemForm': AddItemForm,
        'tasks': tasks,
        'groups': CreateGroupOfTasks.objects.all(),
        'lists': CreateList.objects.all(),
    }
    return render(request, "index.html", context)

@login_required
def add_new_list_view(request, pk_group, list_name):
    pk_group = CreateGroupOfTasks.objects.get(pk=pk_group)
    list_name = CreateList.objects.get(title=list_name)
    form = AddListForm(request.POST or None)



    if request.method == 'POST':
        if 'addlist' in request.POST:
            form1 = AddListForm(request.POST or None)
            if form1.is_valid():
                new_list = form.save(commit=False)
                new_list.whichGroup = pk_group
                new_list.title = list_name
                new_list.save()

        elif 'addgroup' in request.POST:
            form2 = AddGroupForm(request.POST or None)
            if form2.is_valid():
                form2.save()

        elif 'additem' in request.POST:
            form3 = AddItemForm(request.POST or None)
            if form3.is_valid():
                new_task = form3.save(commit=False)
                new_task.whichList = list_name
                new_task.save()
        return redirect(request.path)

    context = {
        'listForm': AddListForm,
        'groupForm': AddGroupForm,
        'itemForm': AddItemForm,
        'tasks': Createtask.objects.all(),
        'groups': CreateGroupOfTasks.objects.all(),
        'lists': CreateList.objects.all(),
        'list_name': list_name
    }
    return render(request, "index.html", context)