from django.urls import path
from . import views

urlpatterns = [
    #Path for getting all data inputs
    path('', views.index, name='index'),

    #Path for getting data from single school
    path('single/<str:schoolName>/', views.singleData, name = 'singleData'),
    
    #Path for uploading data
    path('upload/', views.createData, name = 'createData'),
    
    #Path for sending data to the oracle
    path('oracle/<str:schoolName>/', views.oracle, name = 'oracle'),
]
