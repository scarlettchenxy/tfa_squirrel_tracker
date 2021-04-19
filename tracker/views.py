from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Squirrelinfo
from .utils import stas_png


def add(request):
    if request.method == 'GET':
        return render(request, 'tracker/squirrel_add.html')
    if request.method == 'POST':
        data = {}
        attrs = ['x', 'y', 'uniquesquirrelid', 'Shift', 'Date', 'Age', 'primaryfurcolor',
                  'specificlocation', 'chasing', 'climbing', 'foraging', 'quaas', 'kuks', 'approaches',
                 'indifferent', 'runsfrom'
                 ]
        for attr in attrs:
            data[attr.lower()] = request.POST[attr].strip()
        sighting = Squirrelinfo.objects.create(**data)
        sighting.save()
        return redirect(reverse('tracker:squirrels_position'))

def edit(request, unique_squirrel_id):

    squirrel = Squirrelinfo.objects.filter(uniquesquirrelid=unique_squirrel_id).first()
    method_type = request.method
    edit_attr = ['x', 'y', 'uniquesquirrelid', 'shift', 'date', 'age']
    if method_type == 'POST':
        for attr in edit_attr:
            setattr(squirrel, attr, request.POST[attr].strip())
        squirrel.save()
        squirrel = Squirrelinfo.objects.filter(uniquesquirrelid=unique_squirrel_id).first()
        messages.add_message(request,messages.SUCCESS,'update success')
        return render(request, 'tracker/squirrel_edit.html', context={'squirrel': squirrel})
    else:

        return render(request, 'tracker/squirrel_edit.html', context={'squirrel': squirrel})


def squirrels_position(request):
    squirrels = Squirrelinfo.objects.all()
    paginator = Paginator(squirrels, 15)
    page_number = request.GET.get('page', 1)
    return render(request, 'tracker/squirrel_position.html', context={'all_pages': paginator.get_page(page_number)})


def index(request):
    return render(request, 'tracker/index.html', context={'squirrels': Squirrelinfo.objects.all()})


def stats(request):
    squirrels = Squirrelinfo.objects.all().values()
    primaryfuldata = dict()
    locationdata = dict()
    shiftdata = dict()
    runningdata = dict()
    shiftdata['AM'] = 0
    shiftdata['PM'] = 0
    runningdata['True'] = 0
    runningdata['False'] = 0
    for squirrel in squirrels:
        if squirrel['primaryfurcolor'] in primaryfuldata.keys():
            primaryfuldata[squirrel['primaryfurcolor']] += 1
        else:
            primaryfuldata[squirrel['primaryfurcolor']] = 0
        if squirrel['shift'] == 'AM':
            shiftdata['AM'] += 1
        else:
            shiftdata['AM'] += 1
        if squirrel['running'] == 'True':
            runningdata['True'] += 1
        else:
            runningdata['False'] += 1
        if squirrel['location'] in locationdata.keys():
            locationdata[squirrel['location']] += 1
        else:
            locationdata[squirrel['location']] = 0

    return render(request, 'tracker/squirrel_stats.html', context={
        'shift': stas_png(shiftdata),
        'running': stas_png(runningdata),
        'location': stas_png(locationdata),
        'primary_fur_color': stas_png(locationdata)

    })
