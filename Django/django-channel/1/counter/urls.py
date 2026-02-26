from django.urls import path
from counter.views import CounterView

urlpatterns = [
    path('', CounterView.as_view(), name='counter')
        
]
