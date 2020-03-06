from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView
from rest_framework import routers
from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token 

router = routers.DefaultRouter()

urlpatterns = [
    path('index/', views.index.as_view(), name='index'),

    #path for charts
    url('register/', views.RegisterView.as_view()),

    #Path for home
    url('home/', views.HomePageView.as_view()),
  
    #path for charts
    url('charts/', views.ChartsView.as_view()),

    #Path for signup
    url('login/', views.LoginView.as_view()),

    #Path for getting data from department
    path('single/<str:schoolName>/<str:departmentName>/', views.singleData.as_view(), name = 'singleData'),
    
    #Path for getting multiple departments from single school    
    path('multiple/<str:schoolName>/', views.multipleData.as_view(), name = 'multipleData'),
    
    #Path for uploading data
    path('upload/', views.uploadFile, name = 'uploadFile'),
    
    #Path for sending data to the oracle
    path('markov/', views.testData, name = 'testData'),

    #Path for creating a user
    url('createUser/', views.createUser, name = 'createUser'),

    #Path for logout
    path('logout/', views.userLogout, name = 'userLogout'),

    #Path for giving permission
    path('permission/', views.givePerm, name = 'givePerm'),

]
