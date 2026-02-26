from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class CounterView(View):

    def get(self, request):
        context = {
            'count': 'Hello world',
        }

        return render(request, 'counter/index.html', context)