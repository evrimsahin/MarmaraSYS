from django.contrib import admin
from .models import Student,InternShip,InternShipHiddenFields
from . import models

# Register your models here.
class internShipInLine(admin.StackedInline):
    model = InternShip
    extra = 0

class internShipHiddenInLine(admin.StackedInline):
    model = InternShipHiddenFields
    extra = 0

class Lecturer(admin.ModelAdmin):
    inlines = [internShipInLine,internShipHiddenInLine]
    list_display = ['studentNum','studentName','studentSurname']
    search_fields = ['studentNum','studentName','tcNum','startDate']


admin.site.register(Student,Lecturer)
admin.site.site_header = "MARMARA UNIVERSITESI STAJ YONETIM SISTEMI"
admin.site.site_title= "marmaraSYS"
admin.site.index_title="Staj Yönetim Sistemi"