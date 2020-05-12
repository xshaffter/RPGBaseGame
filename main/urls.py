from django.urls import path, include

from main.views.profile import urlpatterns as profile_urls
from main.views.main import urlpatterns as main_urls
from main.views.authentication import urlpatterns as auth_url
from main.views.character import urlpatterns as character_url

urlpatterns = (
    path('', include(main_urls)),
    path('profile/', include(profile_urls)),
    path('usrauth/', include(auth_url)),
    path('character/', include(character_url)),
)
