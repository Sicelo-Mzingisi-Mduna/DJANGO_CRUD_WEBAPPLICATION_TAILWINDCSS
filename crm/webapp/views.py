from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Customer
from django.http import HttpRequest
# Home page / Landing page
def home(request: HttpRequest):
  return render(request, 'webapp/index.html') 

# Register a User
def register(request: HttpRequest):
  form = CreateUserForm()
  
  if request.method == "POST":
    form = CreateUserForm(request.POST)
    
    if form.is_valid():
      form.save()
      return redirect('login')

  context = {'form': form}
  return render(request, 'webapp/register.html', context = context)

#login a user

def login(request: HttpRequest):
  form = LoginForm()
  if request.method == "POST":
    form = LoginForm(request, data = request.POST)
    
    if form.is_valid():
      username = request.POST.get('username')
      password = request.POST.get('password')
      
      user = authenticate(request, username=username, password=password)
      
      if user is not None:
        auth.login(request, user)
        return redirect('dashboard')
      else :
        form.add_error(None, 'Invalid username or password')
        
  context = {'form': form}
  return render(request, 'webapp/login.html', context = context)