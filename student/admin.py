from django.contrib import admin
from .models import Student,InternShip,InternShipHiddenFields

class internShipInLine(admin.StackedInline):
    model = InternShip
    extra = 0

class internShipHiddenInLine(admin.StackedInline):
    model = InternShipHiddenFields
    extra = 0

class Lecturer(admin.ModelAdmin):
    inlines = [internShipInLine,internShipHiddenInLine]
    list_display = ['user','studentNum','studentName','studentSurname']
    search_fields = ['studentNum','studentName','tcNum','internship__startDate']


admin.site.register(Student,Lecturer)
admin.site.site_header = "MARMARA UNIVERSITESI STAJ YONETIM SISTEMI"
admin.site.site_title= "marmaraSYS"
admin.site.index_title="Staj Yönetim Sistemi"