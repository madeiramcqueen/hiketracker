from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('hikes/', views.hikes_index, name='index'),
    path('hikes/<int:hike_id>/', views.hikes_detail, name='detail'),
    path('hikes/create/', views.HikeCreate.as_view(), name='hikes_create'),
    path('hikes/<int:pk>/update/', views.HikeUpdate.as_view(), name='hikes_update'),
    path('hikes/<int:pk>/delete/', views.HikeDelete.as_view(), name='hikes_delete'),
    path('hikes/<int:hike_id>/add_photo/', views.add_photo, name='add_photo'),
    path('register', views.register_request, name='register'),
    path('registration/logout', views.logout, name='logout'),
    path('registration/login', views.login, name='login'),
]

