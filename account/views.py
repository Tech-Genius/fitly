from django.shortcuts import render, redirect
from . forms import *
from django.contrib import messages
# from django.core.checks import messages
from django.contrib.auth import authenticate, logout, login

# Create your views here.



def register(request):
    form = UserRegistrationForm(request.POST)
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user =  form.cleaned_data.get('username')
            messages.success(request, user + ', Your account has been created sucessfully.')
            return redirect('login')
        else:
            messages.info(request, 'Cannot sign up. Please, refill the form correctly')       
    context = {'form' : form}
    return render(request, 'account/register.html', context)


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
                messages.error(request,'Username Or Password Is Incorrect')

    context = {} 
    return render(request, 'account/login.html', context)  

def userlogout(request):
    logout(request)
    return redirect('index')