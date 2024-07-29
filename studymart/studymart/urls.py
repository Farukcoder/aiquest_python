"""
URL configuration for studymart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Blogs Route
    path('', include('Blogs.urls')),

    # Machine Learning Route
    path('machine_learning/', include('Machine_Learning.urls')),

    # Deep Learning Route
    path('deep_learning/', include('Deep_Learning.urls')),

    # Data Analysis Route
    path('data_analysis/', include('Data_Analysis.urls')),

    # About us route
    path('about_us/', include('About_Us.urls')),
]
