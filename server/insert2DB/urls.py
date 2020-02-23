from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView
from rest_framework import routers
from django.conf.urls import url

router = routers.DefaultRouter()

urlpatterns = [
    #Path for getting all data inputs
    url('home/', views.HomePageView.as_view()),

    #Path for getting data from department
    path('single/<str:schoolName>/<str:departmentName>/', views.singleData, name = 'singleData'),
    
    #Path for getting multiple departments from single school    
    path('multiple/<str:schoolName>/', views.multipleData, name = 'multipleData'),
    
    #Path for uploading data
    path('upload/', views.uploadFile, name = 'uploadFile'),
    
    #Path for sending data to the oracle
    path('markov/', views.testData, name = 'testData'),

    #Path for creating a user
    path('createUser/', views.createUser, name = 'createUser'),

    #Path for login
    path('login/', views.userLogin, name = 'userLogin'),

    #Path for logout
    path('logout/', views.userLogout, name = 'userLogout'),

    #Path for giving permission
    path('permission/', views.givePerm, name = 'givePerm'),

]
