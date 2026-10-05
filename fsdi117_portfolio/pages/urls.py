from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_me_view, name='about_me'),
    path('experience/', views.experience_view, name='experience'),
    path('contact/', views.contact_view, name='contact'),
]
