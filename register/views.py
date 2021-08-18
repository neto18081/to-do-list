from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User

# Create your views here.

def register(response):
  if User.is_authenticated:
    return redirect('/')

  if response.method == 'POST':
    form = RegisterForm(response.POST)
    if form.is_valid():
      form.save()

    return redirect('/login')
  else:
    form = RegisterForm()
  return render(response, 'register/register.html', {'form':form})
