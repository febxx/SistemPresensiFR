from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

@login_required(login_url='/login/')
def dashboard(request):
    context = {
        'nav': 'dashboard'
    }
    return render(request, 'dashboard.html', context)