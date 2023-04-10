from django.contrib import admin
from django.urls import  path 
from . import views


urlpatterns = [
    
    path('students/', views.studentsview.as_view()),
    path('students/<int:pk>/', views.students.as_view()),
    path('details/', views.viewDetails.as_view()),
    path('details/<int:pk>/', views.details.as_view()),
    
   ]