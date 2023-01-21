from django.shortcuts import render, redirect
import os
from .models import Hike
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Home view
def home(request):
    return render(request, 'home.html')

# About view
def about(request):
    return render(request,'about.html')

# My Hikes 
def hikes_index(request):
    hikes = Hike.objects.all()
    return render(request, 'hikes/index.html', {'hikes': hikes})

# Show details of a specific hike 
def hikes_detail(request, hike_id):
    hike = Hike.objects.get(id=hike_id)
    return render(request, 'hikes/detail.html', {'hike': hike})

# Create a new hike 
class HikeCreate(CreateView):
    model = Hike
    fields = '__all__'
    success_url = '/hikes/'

# Update a hike 
class HikeUpdate(UpdateView):
    model = Hike
    fields = '__all__'

# Delete a hike
class HikeDelete(DeleteView):
    model = Hike
    success_url = '/hikes/'