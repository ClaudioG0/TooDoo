from django import forms
from .models import Createtask, CreateGroupOfTasks, CreateList

class AddListForm(forms.Form):
    title = forms.CharField(label="", max_length=40, widget=forms.TextInput(
        attrs={
        'type': 'text', 'class': 'new list fontsize', 'placeholder': 'Add '
                                                                     'List',
    'aria-label': 'add list'}))

    class Meta:
        model = CreateList
        fields = '__all__'



class AddGroupForm(forms.Form):
    title = forms.CharField(label="", max_length=40, widget=forms.TextInput(
        attrs={
        'type': 'text', 'class': 'new list font_size add_group', 'placeholder': 'Add Group',
    'aria-label': 'add group'}))

    class Meta:
        model = CreateGroupOfTasks
        fields = "__all__"



class AddItemForm(forms.Form):
    title = forms.CharField(label="", max_length=40, widget=forms.TextInput(
        attrs={
        'type': 'text', 'class': 'new item', 'placeholder': 'Add item',
    'aria-label': 'add list'}))

    class Meta:
        model = Createtask
        fields = "__all__"


