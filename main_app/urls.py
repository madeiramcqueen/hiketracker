from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('hikes/', views.hikes_index, name='index'),
    path('hikes/<int:hike_id>/', views.hikes_detail, name='detail'),
]

