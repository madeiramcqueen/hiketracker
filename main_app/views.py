from django.shortcuts import render
from django.http import HttpResponse

class Hike:
    def __init__(self, name, location, length, elevation, level, description):
        self.name = name
        self.location = location
        self.length = length
        self.elevation = elevation
        self.level = level
        self.description = description
        
hikes = [
    Hike('Mount Si', 'North Bend, WA', '8 miles', '3150 ft', 'Difficult', 'Very steep but rewarding!'),
]

# Home view
def home(request):
    return HttpResponse('<h1> Welcome to  your Hike Tracker! </h1>')

# About view
def about(request):
    return render(request,'about.html')

# My Hikes view
def hikes_index(request):
    return render(request, 'hikes/index.html', {'hikes': hikes})
