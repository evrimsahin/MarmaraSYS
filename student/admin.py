from django.contrib import admin
from .models import Student

# Register your models here.

class Lecturer(admin.ModelAdmin):

    list_display = ['studentNum','studentName','studentSurname']
    search_fields = ['studentNum','studentName','tcNum','startDate']
    class Meta:
        model = Student

admin.site.register(Student,Lecturer)