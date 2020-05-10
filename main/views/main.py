from django.shortcuts import render


# Create your views here.
from django.urls import path


def dashboard(request):
    context = {
        'model_name': 'Login'
    }
    return render(request, 'models/profile/index.html', context=context)


urlpatterns = [
    path('', dashboard, name="dashboard")
]
