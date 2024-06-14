from django.contrib import admin
from lessons.models import Course, Lesson, Task, TaskSubmission

# Register your models here.

@admin.register(Course) # регистрирация модели Course в административной панели
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Lesson) # регистрирация модели Lesson в административной панели
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course') # отображение названия урока и курса в списке уроков в админ. панели 

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass

@admin.register(TaskSubmission)
class TaskSubmissionAdmin(admin.ModelAdmin):
    list_filter = ["task"]
    list_display = ['task']