"""
URL configuration for StudyWala project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
    path('', include('dashboard.urls')),  # root URL points to dashboard app
    path('projects/', include('projects.urls')),  # root URL points to projects app
    path('pyqs/', include('pyqs.urls')),  # root URL points to pyqs app
    path('resources/', include('resources.urls')),  # root URL points to resources app
    path('accounts/', include('accounts.urls')),
    path('community/', include('community.urls')),  # root URL points to community app
]
