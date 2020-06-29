from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from .forms import CreateUserForm, UpdateUserForm
# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request, 'Invalid Credientials')
            return redirect('login')
    else:
        return render(request, 'accounts/loginpage.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def register(request):
    user_form = CreateUserForm()
    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('index')
    context = {
        'user_form': user_form,
    }
    return render(request, 'accounts/registerpage.html', context)


def update_user(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('students_list')
    else:
        user_form = UpdateUserForm(instance=user)

    context = {
        'user_form': user_form,
    }
    return render(request, 'accounts/updatepage.html', context)


def delete_user(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return HttpResponse('No user')
    context = {
        'student': user
    }
    return render(request, 'accounts/confirmationpage.html', context)


def confirm_delete_user(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
    except User.DoesNotExist:
        return HttpResponse('No user')
    messages.success(request, 'Delete successfull')
    return redirect('students_list')
