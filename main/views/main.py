from django.shortcuts import render


# Create your views here.
from django.urls import path


def dashboard(request):
    profile = request.user.profile
    context = {
        'title': 'Menú principal',
        'model_name': 'Dashboard',
        'model': profile
    }
    return render(request, 'models/dashboard/index.html', context=context)


urlpatterns = [
    path('', dashboard, name="dashboard")
]
