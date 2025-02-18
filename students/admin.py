from django.contrib import admin
from .models import Student, Course, Progress

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Progress)
