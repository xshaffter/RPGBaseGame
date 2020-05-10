from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    auth = None
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput())
    password = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs=dict(type='password')))

    def clean(self):
        data = super(LoginForm, self).clean()
        username = data["username"]
        password = data["password"]

        user = authenticate(username=username, password=password)

        if not user:
            raise forms.ValidationError("Usuario y/o contraseña incorrecto/s")

        self.auth = user
        return data
