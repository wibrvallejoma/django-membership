"""django_membership URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from plans.views import home, plan, join, checkout
from users.views import SignUp, settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('plans/<int:pk>', plan, name='plan'),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/signup', SignUp.as_view(), name='signup'),
    path('join', join, name='join'),
    path('checkout', checkout, name='checkout'),
    path('auth/settings', settings, name='settings'),
]
