"""
URL configuration for shifu project.
"""
#определение URL-адресов для Django-приложения, и связывание их с соответствующими функциями-представлениями (views)

from django.contrib import admin #импортирт модуля административной панели, чтобы подключить её к URL-адресам
from django.urls import path #импорт функции path для определения URL-шаблонов
from lessons import views #импорт функций-представлений из приложения lessons

urlpatterns = [
    path('admin/', admin.site.urls), #определение URL-шаблона для административной панели 
    path('api/courses/', views.courses, name='courses'), # определение URL-шаблона для получения списка курсов
    path('api/lessons/<int:course_id>', views.lessons), #Определение URL-шаблона для получения уроков, относящихся к конкретному курсу
    path('api/tasks/<int:lesson_id>', views.tasks),# определение URL-шаблона для получения заданий, относящихся к определённому уроку
    path('get_audio/<int:task_id>', views.get_audio), #получение аудиофайла, связанного с заданием
    path('upload_audio/<int:task_id>', views.upload_audio),#загрузка аудио, записанного пользователем
]
