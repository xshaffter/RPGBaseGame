from django import views
from django.shortcuts import render, get_object_or_404
from django.urls import path

from main.models import Character


def index(request, id_character):
    character = get_object_or_404(Character, pk=id_character)
    context = {
        'title': request.user.username,
        'model_name': 'Personaje',
        'model': character
    }
    return render(request, 'models/character/index.html', context=context)


urlpatterns = [
    path('<int:id_character>/', index, name="character_index")
]
