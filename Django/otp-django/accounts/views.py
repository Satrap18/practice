from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class Login(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')



class Register(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'register.html')

