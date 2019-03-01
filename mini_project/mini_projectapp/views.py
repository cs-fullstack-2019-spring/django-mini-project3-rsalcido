from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import TimeCardForm #forms
from .models import TimeCardModel
# functions that lead from path created
def index(request):
        form = TimeCardForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('index')
# time stamps
def Teachers(request, id):
    return render(request, 'mini_projectapp/index.html')

# records
def SchoolsDatabase (request, id):
    return render(request, 'mini_projectapp/index.html')
def add(request):
    form = TimeCardForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'mini_projectapp/Timecard_record.html', context)


def edit(request, id):
    tstamps = get_object_or_404(TimeCardModel, pk=id)
    edit_form = TimeCardForm(request.POST or None, instance=tstamps)
    if edit_form.is_valid():
        edit_form.save()
        return redirect('index')
    context = {
        'form': edit_form
    }
    return render(request, 'mini_projectapp/edit.html', context)
# function that leads to my time edit form
def delete(request, id):
    tstamps = get_object_or_404(TimeCardModel, pk=id)
    if request.method == 'POST':
        tstamps.delete()
        return redirect('index')
    context = {
        'teacher': tstamps
    }
    return render(request, 'mini_projectapp/deletes.html', context)
# function that leads to a deletes html form