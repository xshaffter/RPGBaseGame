from django.shortcuts import render


# Create your views here.
def dashboard(request):
    context = {
        'model_name': 'Login'
    }
    return render(request, 'models/profile/index.html', context=context)
