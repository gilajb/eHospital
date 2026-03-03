from django.contrib import admin
from django.urls import path, include #NOTE: Import include for app urls

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('HospitalApp.urls')) #NOTE: Include app urls
]
