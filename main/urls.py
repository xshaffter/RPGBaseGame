from django.urls import path, include

from main.views import main as main_views, authentication as auth_views

urlpatterns = [
    path('', main_views.dashboard, name="dashboard"),
    path('login/', auth_views.LoginView.as_view(), name="usr_login"),
    path('logout/', auth_views.logout_view, name="usr_logout"),
]
