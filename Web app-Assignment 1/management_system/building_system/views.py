from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .models import *

from .forms import *


def index(request):
    return render(request, 'inv/index.html')


def display_electrical(request):
    items = Electrical.objects.all()
    context = {
        'items': items,
        'header': 'Electrical',
    }
    return render(request, 'inv/index.html', context)


def display_mechanical(request):
    items = Mechanical.objects.all()
    context = {
        'items': items,
        'header': 'Mechanical',
    }
    return render(request, 'inv/index.html', context)


def display_cleaning(request):
    items = Cleaning.objects.all()
    context = {
        'items': items,
        'header': 'Cleaning',
    }
    return render(request, 'inv/index.html', context)


def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return render(request, 'inv/add_new.html', {'form': form})


def add_electrical(request):
    return add_item(request, ElectricalForm)


def add_mechanical(request):
    return add_item(request, MechanicalForm)


def add_cleaning(request):
    return add_item(request, CleaningForm)


def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'inv/edit_item.html', {'form': form})


def edit_electrical(request, pk):
    return edit_item(request, pk, Electrical, ElectricalForm)


def edit_mechanical(request, pk):
    return edit_item(request, pk, Mechanical, MechanicalForm)


def edit_cleaning(request, pk):
    return edit_item(request, pk, Cleaning, CleaningForm)


def delete_electrical(request, pk):
    template = 'inv/index.html'
    Electrical.objects.filter(id=pk).delete()

    items = Electrical.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_mechanical(request, pk):
    template = 'inv/index.html'
    Mechanical.objects.filter(id=pk).delete()

    items = Mechanical.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_cleaning(request, pk):
    template = 'inv/index.html'
    Cleaning.objects.filter(id=pk).delete()

    items = Cleaning.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)
