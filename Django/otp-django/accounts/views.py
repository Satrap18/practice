from django.shortcuts import render
from django.views.generic import View
from accounts.forms import LoginForms
from django.contrib.auth import login, authenticate, logout
# Create your views here.

class Login(View):

    def get(self, request, *args, **kwargs):
        form = LoginForms()
        return render(request, 'login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForms()
        clean_data = form.cleaned_data
        username = clean_data['username']
        password = clean_data['password']
        user = (username, password)
        login(request, user)

class Register(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'register.html')

