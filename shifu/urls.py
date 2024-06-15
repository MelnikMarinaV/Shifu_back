"""
URL configuration for shifu project.
"""
from django.contrib import admin
from django.urls import path
from lessons import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/courses/', views.courses, name='courses'), 
    path('lessons/<int:course_id>', views.lessons),
]
