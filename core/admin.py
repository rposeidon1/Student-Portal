from django.contrib import admin
from .models import Course, Student

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["course_title", "duration"]
    search_fields = ["course_title"]

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "course", "created_at"]
    search_fields = ["name", "email"]
    list_filter = ["course"]