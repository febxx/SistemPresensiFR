import re
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from apps.authentication.forms import LoginForm

# Create your views here.
def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == 'POST':
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                msg = 'Invalid user'
        else:
            msg = 'Error validating'
    context = {
        'form': form,
        'msg': msg,
    }
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('index')