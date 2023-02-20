"""quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

import quiz_pages.views as views

app_name = 'quiz_pages'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:theme_id>/', views.quiz, name='quiz'),
    path('<int:theme_id>/results/', views.results, name='results'),
    path('check_form/', views.check_form, name='check_form'),
    path('add_quiz/', views.add_quiz, name='add_quiz'),
]
