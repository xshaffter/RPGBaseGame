from django import views
from django.shortcuts import render, get_object_or_404
from django.urls import path

from main.models import Profile


def index(request):
    profile = request.user.profile
    context = {
        'title': request.user.username,
        'model_name': 'Perfil',
        'model': profile
    }
    return render(request, 'models/profile/index.html', context=context)


urlpatterns = [
    path('', index, name="profile_index")
]
