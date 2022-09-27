from django.contrib import admin
from .models import Student

admin.site.site_header = 'STUDENT MANAGEMENT SYSTEM'
admin.site.site_title = 'student management system'
admin.site.index_title = 'Student Management app'


# Register your models here.
admin.site.register(Student)