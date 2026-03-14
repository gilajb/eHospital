from django.contrib import admin
from django.urls import path, include #NOTE: This imports the path and include functions from the django.urls module, which are used to define URL patterns for the application.
from HospitalApp import views #NOTE: This imports the views module from the HospitalApp application, which contains the view functions that will handle the requests for the specified URLs.

urlpatterns = [  #NOTE: This is the main URL configuration for the HospitalApp project. It includes paths for the admin interface and the home and starter views.
    path('admin/', admin.site.urls),
    
    path('home/', views.home, name='home'),
    
    path('', views.home, name='home'), #NOTE: The empty path '' is also mapped to the home view, making it the default page when the user visits the root URL of the application.
    
    path('starter/', views.starter, name='starter'), 
    
    path('appointment/', views.appointment, name='appointment'),
    
    path('show/', views.show, name='show'),
    
    path('delete/<int:id>/', views.delete), #NOTE: This URL pattern includes a dynamic segment <int:id>, which captures an integer value from the URL and passes it as an argument to the delete view function. This allows the application to identify which appointment to delete based on its unique ID.

    path('showpatient/', views.showpatient, name='showpatient'),
]