from django.contrib import admin

# Register your models here.

from start.models import Day, Time, Course, Faculty, Takes

admin.site.register(Day)
admin.site.register(Time)
admin.site.register(Course)
admin.site.register(Faculty)
admin.site.register(Takes)