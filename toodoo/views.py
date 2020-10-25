from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from toodooLogic.forms import AddListForm, AddGroupForm, AddItemForm
from toodooLogic.models import Createtask, CreateGroupOfTasks, CreateList

@login_required
def index(request):
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