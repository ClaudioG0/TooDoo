from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from toodooLogic.forms import AddListForm, AddGroupForm, AddItemForm
from toodooLogic.models import Createtask, CreateGroupOfTasks, CreateList

@login_required
def index(request):


    if request.method == 'POST':
        if 'addlist' in request.POST:
            form1 = AddListForm(request.POST)
            if form1.is_valid():
                form1.save(commit=False)
                form1.whichGroup = 1
                form1.save()
        elif 'addgroup' in request.POST:
            form2 = AddGroupForm(request.POST)
            if form2.is_valid():
                form2.save()

        elif 'additem' in request.POST:
            form3 = AddItemForm(request.POST)
            if form3.is_valid():
                form3.save()
        return redirect('/')

    context = {
        'listForm': AddListForm,
        'groupForm': AddGroupForm,
        'itemForm': AddItemForm,
        'tasks': Createtask.objects.all(),
        'groups': CreateGroupOfTasks.objects.all(),
        'lists': CreateList.objects.all(),
    }
    return render(request, "index.html", context)

def add_new_list_view(request, pk_group):
    pk_group = CreateGroupOfTasks.objects.get(pk=pk_group)
    form = AddListForm(request.POST or None)

    context = {
        'listForm': AddListForm,
        'groupForm': AddGroupForm,
        'itemForm': AddItemForm,
        'tasks': Createtask.objects.all(),
        'groups': CreateGroupOfTasks.objects.all(),
        'lists': CreateList.objects.all(),
    }

    if request.POST:
        if form.is_valid():
            new_list = form.save(commit=False)
            new_list.whichGroup = pk_group
            new_list.save()
            return render(request, 'index.html', context)