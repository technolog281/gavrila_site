from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stat.html', views.stat, name='stat'),
    path('report/', views.report),
]
