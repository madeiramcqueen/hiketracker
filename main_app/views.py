from django.shortcuts import render, redirect
from .models import Hike, Photo
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import uuid
import boto3
import os

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

# Add a photo
def add_photo(request, hike_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # if error
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # assign to hike_id or hike object
            Photo.objects.create(url=url, hike_id=hike_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', hike_id=hike_id)

# Register a user
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("about")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})

# Logout
def logout(request):
    return render(request, 'registration/logout.html')