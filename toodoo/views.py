from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from toodooLogic.forms import AddListForm, AddGroupForm, AddItemForm
from toodooLogic.models import Createtask, CreateGroupOfTasks, CreateList

@login_required
def index(request):

    if request.method == 'POST':
        if 'addlist' in request.POST:
            form = AddListForm(request.POST)
            if form.is_valid():
                form.save()

        elif 'addgroup' in request.POST:
            form = AddListForm(request.POST)
            if form.is_valid():
                form.save()

        elif 'additem' in request.POST:
            form = AddListForm(request.POST)
            if form.is_valid():
                form.save()

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

def results(request, list_id):
    listOfTasks = get_object_or_404(CreateGroupOfTasks,
                                    pk=list_id)
    return render(request, 'justTest.html', {"listOfTasks": listOfTasks})