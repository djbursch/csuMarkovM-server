from django.urls import path
from . import views

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
    path('oracle/', views.testOracle, name = 'testOracle'),

    #Path for creating a user
    path('createUser/', views.createUser, name = 'createUser'),

    #Path for login
    path('login/', views.userLogin, name = 'userLogin'),

    #Path for logout
    path('logout/', views.userLogout, name = 'userLogout'),

    #Path for logout
    path('permission/', views.givePerm, name = 'givePerm'),
]
