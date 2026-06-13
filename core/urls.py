from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("students/", views.students_list, name="students_list"),
    path("students/add/", views.student_add, name="student_add"),
    path("students/<int:student_id>/edit/", views.student_edit, name="student_edit"),
    path("students/<int:student_id>/delete/", views.student_delete, name="student_delete"),
    path("courses/", views.courses_list, name="courses_list"),
    path("courses/add/", views.course_add, name="course_add"),
    path("courses/<int:course_id>/edit/", views.course_edit, name="course_edit"),
    path("courses/<int:course_id>/delete/", views.course_delete, name="course_delete"),
    path("students/search/", views.student_search, name="student_search"),
]
