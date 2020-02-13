from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('single/<int:array_id>/', views.singleArray, name = 'singleArray'),
    path('single/upload/', views.createArray, name = 'createArray'),
]
