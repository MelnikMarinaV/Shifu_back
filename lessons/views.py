from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from lessons.models import Course, Lesson
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
