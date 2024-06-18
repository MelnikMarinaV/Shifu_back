from django.http import JsonResponse, HttpResponse
from lessons.models import Course, Lesson, Task
from django.views.decorators.csrf import csrf_exempt


#Обрабатывает GET-запросы к URL /api/courses/
def courses(request):
    courses = Course.objects.all()#Получает все объекты модели `Course` из базы данных
    return JsonResponse({ #Формирует JSON-ответ, содержащий список всех курсов с их id и title
        'courses': [
            {'id': course.id, 'title': course.title} for course in courses
        ]
    })

#Обрабатывает GET-запросы к URL /api/lessons/<course_id>/
@csrf_exempt
def lessons(request, course_id):
    course = Course.objects.get(id=course_id) #Получает объект Course  с заданным course_id
    lessons = Lesson.objects.filter(course=course)#Получает все объекты модели Lesson, связанные с этим курсом
    return JsonResponse({ #  Формирует JSON-ответ, содержащий список уроков с их id и title
            'lessons': [
                {'id': lesson.id, 'title': lesson.title} for lesson in lessons
            ]
        })

#Обрабатывает GET-запросы к URL /api/tasks/<lesson_id>/
def tasks(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)#Получает объект Lesson  с заданным lesson_id
    tasks = Task.objects.filter(lesson=lesson)#Получает все объекты модели Task, связанные с этим уроком
    return JsonResponse({ #Формирует JSON-ответ, содержащий список заданий с их id, title(сам контент упражнения) и task_description(ответ к заданию)
            'tasks': [
                {'id': task.id, 
                 'title': task.title,
                 'description': task.task_description
                } for task in tasks
            ],
            'description': lesson.description,#описание урока-теория
            'title': lesson.title#название урока
        })


#получение аудио файла произношения фраз(расположены локально)
#Обрабатывает GET-запросы к URL /get_audio/<task_id>/
@csrf_exempt
def get_audio(request, task_id):
    path= f'C:/Users/Admin/Documents/back/lessons/static/audios/task{task_id}.mp3'#путь до файла
    with open(path, 'rb') as f:
            audio = f.read()
    return HttpResponse(audio, content_type='audio/mpeg')#Возвращает содержимое аудиофайла


#обрабатывает загрузку аудиофайлов от пользователя, которые связаны с определенным заданием
#Обрабатывает POST-запросы к URL /upload_audio/<task_id>/
@csrf_exempt
def upload_audio(request, task_id):
    if 'audio' in request.FILES: #Ожидает получить аудиофайл в поле audio тела запроса
        audio_file = request.FILES['audio']
        path= f'C:/Users/Admin/Documents/back/lessons/static/submissions/task{task_id}.mp3'
        with open(path, 'wb') as destination:#Сохраняет полученный аудиофайл на сервере по пути
            for chunk in audio_file.chunks():
                destination.write(chunk)  
        return JsonResponse({'message': 'Audio file saved successfully'})
    else:
        return JsonResponse({'error': 'No audio file found in the request'}, status=400)


