from django.contrib.auth.decorators import login_required
from django.contrib.auth import  login,logout
from django.shortcuts import redirect, render

from .forms import UserRegistrationForm,UserLoginForm
def register (request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user =form.save()
            return redirect('login')
    else:
            form=UserRegistrationForm()
    return render (request,'register.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request,request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect('buttonpage')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect ('login')
def buttonpage(request):
    return render(request,'buttonpage.html')

def order(request):
    return render(request,'order.html')