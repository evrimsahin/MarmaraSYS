from django.contrib import admin
from .models import Student,InternShip,InternShipHiddenFields
from django.contrib.admin import SimpleListFilter
from django.db.models import Q


class internShipInLine(admin.StackedInline):
    model = InternShip
    extra = 0

class internShipHiddenInLine(admin.StackedInline):
    model = InternShipHiddenFields
    extra = 0


class ScrapeStatusFilter(SimpleListFilter):
    title = 'Öğrenci Paneli'
    parameter_name = 'tcNum'

    def lookups(self, request, model_admin):
        return [
            ('öğrenci', 'Öğrenci')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'öğrenci':
            return queryset.filter(~Q(tcNum=''))
        if self.value():
            return queryset.distinct().filter(tcNum=True)


class Lecturer(admin.ModelAdmin):
        inlines = [internShipInLine,internShipHiddenInLine]
        list_display = ['user','studentNum','studentName','studentSurname']
        search_fields = ['studentNum','studentName','tcNum','internship__startDate']
        list_filter = ['internship__internshipType','internship__internshipAbroadOrDomestic',ScrapeStatusFilter]


admin.site.register(Student,Lecturer)
admin.site.site_header = "MARMARA UNIVERSITESI STAJ YONETIM SISTEMI"
admin.site.site_title= "marmaraSYS"
admin.site.index_title="Staj Yönetim Sistemi"