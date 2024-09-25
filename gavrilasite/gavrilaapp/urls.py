from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('stat.html', views.stat, name='stat'),
    path('report', views.report),
    path('main.html', views.main, name='main'),
]
