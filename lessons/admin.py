from django.contrib import admin
from lessons.models import Course, Lesson, Task, TaskSubmission

# Register your models here.

@admin.register(Course) # регистрирация модели Course в административной панели
class CourseAdmin(admin.ModelAdmin):
    list_display=['title'] #отображение названия курса в списке моделей в административной панели


@admin.register(Lesson) # регистрирация модели Lesson в административной панели
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_course_title'] #отображение названия урока и названия курса, к которому он привязан
    def get_course_title(self, obj): #возвращает название курса для урока
        if obj.course:
            return obj.course.title
        else:
            return '-'  # Если курс не указан
    get_course_title.short_description = 'Course'  # Название колонки в административной панели

@admin.register(Task) #регистрация модели задания
class TaskAdmin(admin.ModelAdmin):
    pass

# @admin.register(TaskSubmission)
# class TaskSubmissionAdmin(admin.ModelAdmin):
#     list_filter = ["task"]
#     list_display = ['task']