from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm, LoginUserForm


def login_view(request):
    next = request.GET.get('next')
    form = LoginUserForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)

        if next:
            return redirect(next)

        return redirect("/")


    context = {
        'form': form
    }

    return render(request, 'signIn.html', context)



def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        new_user = authenticate(username=user.username, password=password)

        login(request, new_user)

        if next:
            return redirect(next)

        return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'signUp.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')