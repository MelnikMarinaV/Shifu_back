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
