from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from home.forms import ShiftForm

from home.models import Shift

def index(request):
    return render(request, 'index.html')

@login_required(login_url='/login/')
def dashboard(request):
    context = {
        'nav': 'dashboard'
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='/login/')
def shift(request):
    shifts = Shift.objects.all()
    if request.method == 'POST':
        sh = Shift.objects.filter(id_shift=request.POST['id_shift']).values_list('id', flat=True)
        if sh.exists():
            ids = Shift.objects.get(id=int(sh[0]))
            form = ShiftForm(request.POST, instance=ids)
            if form.is_valid():
                form.save()
        else:
            form = ShiftForm(request.POST or None)
            if form.is_valid():
                form.save()
    context = {'shifts': shifts}
    return render(request, 'shift.html', context)

def delete_shift(request, id):
    Shift.objects.get(id=id).delete()
    return redirect('shift')