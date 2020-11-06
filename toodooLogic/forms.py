from django import forms
from .models import Createtask, CreateGroupOfTasks, CreateList


class AddListForm(forms.ModelForm):
    title = forms.CharField(label="", max_length=40, widget=forms.TextInput(
        attrs={
            'type': 'text', 'class': 'new list fontsize', 'placeholder':
                'Add List',
            'aria-label': 'add list', 'name': 'titleTask'}))

    class Meta:
        model = CreateList
        fields = ['title']


class AddGroupForm(forms.ModelForm):
    title = forms.CharField(label=" ",  max_length=40, \
                                                     widget=forms.TextInput(
        attrs={
        'type': 'text', 'class': 'new list font_size add_group', 'placeholder': 'Add Group',
    'aria-label': 'add group', 'name': 'titleGroup'}))

    class Meta:
        model = CreateGroupOfTasks
        fields = ['title']




class AddItemForm(forms.ModelForm):
    title = forms.CharField(label="", max_length=40, widget=forms.TextInput(
        attrs={
        'type': 'text', 'class': 'new item', 'placeholder': 'Add item',
    'aria-label': 'add list'}))

    class Meta:
        model = Createtask
        fields = ['title']



