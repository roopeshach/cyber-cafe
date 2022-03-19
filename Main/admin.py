from django.contrib import admin

# Register your models here.
from .models import Course, UserLog , TimePeriod, Student

admin.site.register(Course)
admin.site.register(UserLog)
admin.site.register(TimePeriod)
admin.site.register(Student)
