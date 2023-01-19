from django.shortcuts import render
from django.http import HttpResponse
from .models import Hike

# Home view
def home(request):
    return HttpResponse('<h1> Welcome to  your Hike Tracker! </h1>')

# About view
def about(request):
    return render(request,'about.html')

# My Hikes view
def hikes_index(request):
    hikes = Hike.objects.all()
    return render(request, 'hikes/index.html', {'hikes': hikes})

def hikes_detail(request, hike_id):
    hike = Hike.objects.get(id=hike_id)
    return render(request, 'hikes/detail.html', {'hike': hike})
