from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# from django.contrib.auth.forms import UserCreationForm

from .models import *
from .forms  import AccountsForm, UserForm
# from .forms  import CreateUserForm
# from .forms import OrderForm
# from .filters import OrderFilter

def registerPage(request):

    if request.user.is_authenticated: # already logged in
        messages.warning(request, "Sorry, [" + request.user.username + "] already logged in")
        return redirect('/')

    if request.method == "POST":
        formUser    = UserForm(request.POST)
        formAccount = AccountsForm(request.POST)
        # formAccount = AccountsForm(request.POST)
        # if all([formUser.is_valid(), formAccount.is_valid(),]):
        if formUser.is_valid() and formAccount.is_valid():
            user    = formUser.save()
            account = formAccount.save(commit=False)
            account.user = user
            formAccount.save()
            messages.success(request, 'Account created for ' + user.username)
            username = formUser.cleaned_data['username']
            password = formUser.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            print("username=", username, "password=", password)
            print("user=", user)
            login(request, user)
            # return redirect('/accounts/login/')
            return redirect('/')
        else:
            messages.warning(request, "Sorry, field verification failed")

    context = {'formUser':UserForm,'formAccount':AccountsForm,}
    return render(request, 'accounts/register.html', context)


def loginPage(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            messages.success(request, username + ' logged in')
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request, "Sorry, username or password incorrect")

    form = AuthenticationForm()
    if request.user.is_authenticated: # logged in
        return redirect('/accounts/logout/')
    context = {'form':form}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    messages.success(request, '[' + request.user.username + '] logged out')
    logout(request)
    return redirect('/accounts/login/')
