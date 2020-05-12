from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, path

from django.views import View

from main.forms import LoginForm


def redirect(name, kwargs=None):
    if kwargs is None:
        kwargs = dict()
    return HttpResponseRedirect(reverse(name, kwargs=kwargs))


class LoginView(View):
    login_template = "authentication/login.html"

    def get(self, request):
        form = LoginForm()
        context = {
            'model_name': 'Login',
            'form': form
        }
        return render(request, self.login_template, context=context)

    def post(self, request):
        form = LoginForm(request.POST)
        context = {
            'model_name': 'Login',
            'form': form
        }

        if form.is_valid():
            login(request, user=form.auth)
            return redirect("dashboard")

        return render(request, self.login_template, context=context)


def logout_view(request):
    logout(request)
    return redirect("usr_login")


urlpatterns = [
    path('login/', LoginView.as_view(), name="usr_login"),
    path('logout/', logout_view, name="usr_logout"),
]
