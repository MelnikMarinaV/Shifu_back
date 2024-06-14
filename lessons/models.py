from django.db import models

class Course(models.Model): #Модель курса - один курс по материалам HSK-1
    title = models.CharField(max_length=200) 

class Lesson(models.Model): #Модель урока 
    title = models.CharField(max_length=200) #Каждый урок имеет собственное название
    description = models.TextField(default='', null=True, blank=True) #Описание урока-здесь теоретические материалы к уроку
    #связь между моделями Lesson и Course (урок принадлежиткурсу).
    #models.ForeignKey:Устанавливает отношение "многие-к-одному" (много уроков могут принадлежать одному курсу).
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.SET_NULL)

class Task(models.Model): #Задания к урокам
    title = models.CharField(max_length=200)
    #связь "многие-к-одному" между моделями Task и Lesson.  Одна задача может принадлежать только одному уроку,
    # а у одного урока может быть много задач. 
    lesson = models.ForeignKey(Lesson, null=True, blank=True, on_delete=models.SET_NULL)
    task_description = models.TextField(default='')#Описание задания - будет хранить "ответ" на задания по аудированию
    def __str__(self) -> str: #Для удобного представления задания - отображается своим именем
        return self.title
    
class TaskSubmission(models.Model): #Ответы на задания
    #Устанавливается связь "многие-к-одному" с моделью Task, у одного ответа (TaskSubmission) может быть только одна связанная задача
    # (Task), но у одной задачи может быть много ответов
    task = models.ForeignKey(Task, null=True, blank=True, on_delete=models.SET_NULL)
    comment = models.TextField(default='', null=True, blank=True) #хранения текстового комментария к ответу (например, от преподавателя)
    result_file = models.CharField(max_length=200, null=True, blank=True) #поле для хранения пути к файлу, который пользователь загрузил в качестве ответа