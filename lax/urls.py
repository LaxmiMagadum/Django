from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='lax-home'),
    path('about/', views.about, name='lax-about'),
]