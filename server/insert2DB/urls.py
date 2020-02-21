from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    #Path for getting all data inputs
    path('', views.index, name='index'),

    #Path for getting data from department
    path('single/<str:schoolName>/<str:departmentName>/', views.singleData, name = 'singleData'),
    
    #Path for getting multiple departments from single school    
    path('multiple/<str:schoolName>/', views.multipleData, name = 'multipleData'),
    
    #Path for uploading data
    path('upload/', views.uploadData, name = 'uploadData'),
    
    #Path for sending data to the oracle
    path('markov/', views.testMarkov, name = 'testMarkov'),

    #Path for creating a user
    path('createUser/', views.createUser, name = 'createUser'),

    #Path for login
    path('login/', views.userLogin, name = 'userLogin'),

    #Path for logout
    path('logout/', views.userLogout, name = 'userLogout'),

    #Path for giving permission
    path('permission/', views.givePerm, name = 'givePerm'),

    #Path for home
    path('home/', TemplateView.as_view(template_name="home.html"), name = "home")
]
