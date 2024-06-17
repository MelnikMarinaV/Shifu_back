from django.http import JsonResponse, HttpResponse
from lessons.models import Course, Lesson, Task
from django.views.decorators.csrf import csrf_exempt


def courses(request):
    courses = Course.objects.all()
    return JsonResponse({
        'courses': [
            {'id': course.id, 'title': course.title} for course in courses
        ]
    })

@csrf_exempt
def lessons(request, course_id):
    course = Course.objects.get(id=course_id)
    lessons = Lesson.objects.filter(course=course)
    return JsonResponse({
            'lessons': [
                {'id': lesson.id, 'title': lesson.title} for lesson in lessons
            ]
        })

def tasks(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    tasks = Task.objects.filter(lesson=lesson)
    return JsonResponse({
            'tasks': [
                {'id': task.id, 
                 'title': task.title,
                 'description': task.task_description
                } for task in tasks
            ],
            'description': lesson.description,
            'title': lesson.title
        })


#получение аудио файла произношения фраз(расположены локально)
@csrf_exempt
def get_audio(request, task_id):
    path= f'C:/Users/Admin/Documents/back/lessons/static/audios/task{task_id}.mp3'
    with open(path, 'rb') as f:
            audio = f.read()
    return HttpResponse(audio, content_type='audio/mpeg')

@csrf_exempt
def upload_audio(request, task_id):
    if 'audio' in request.FILES:
        audio_file = request.FILES['audio']
        path= f'C:/Users/Admin/Documents/back/lessons/static/submissions/task{task_id}.mp3'
        print(audio_file.size)
        with open(path, 'wb') as destination:
            for chunk in audio_file.chunks():
                destination.write(chunk)  
        return JsonResponse({'message': 'Audio file saved successfully'})
    else:
        return JsonResponse({'error': 'No audio file found in the request'}, status=400)


