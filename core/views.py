import csv

from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CourseForm, StudentForm
from .models import Course, Student


def admin_required(user):
    return user.is_superuser or user.groups.filter(name="Admin").exists()


@login_required
def dashboard(request):
    context = {
        "total_students": Student.objects.count(),
        "total_courses": Course.objects.count(),
        "recent_students": Student.objects.order_by("-created_at")[:5],
    }
    return render(request, "core/dashboard.html", context)


@login_required
def students_list(request):
    all_students = Student.objects.all()
    paginator = Paginator(all_students, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "core/students_list.html", {"students": page_obj})


@login_required
@user_passes_test(admin_required)
def student_add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("students_list")
    else:
        form = StudentForm()
    return render(request, "core/student_form.html", {"form": form})


@login_required
@user_passes_test(admin_required)
def student_edit(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("students_list")
    else:
        form = StudentForm(instance=student)
    return render(request, "core/student_form.html", {"form": form})


@login_required
@user_passes_test(admin_required)
def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        student.delete()
        return redirect("students_list")
    return render(request, "core/student_confirm_delete.html", {"student": student})


@login_required
def courses_list(request):
    all_courses = Course.objects.all()
    paginator = Paginator(all_courses, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "core/courses_list.html", {"courses": page_obj})


@login_required
@user_passes_test(admin_required)
def course_add(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("courses_list")
    else:
        form = CourseForm()
    return render(request, "core/course_form.html", {"form": form})


@login_required
@user_passes_test(admin_required)
def course_edit(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect("courses_list")
    else:
        form = CourseForm(instance=course)
    return render(request, "core/course_form.html", {"form": form})


@login_required
@user_passes_test(admin_required)
def course_delete(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        course.delete()
        return redirect("courses_list")
    return render(request, "core/course_confirm_delete.html", {"course": course})


@login_required
def student_search(request):
    query = request.GET.get("q", "").strip()
    students = Student.objects.filter(
        Q(name__icontains=query)
        | Q(email__icontains=query)
        | Q(course__course_title__icontains=query)
    )
    return render(request, "core/partials/student_results.html", {"students": students})


@login_required
def export_students_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="students.csv" '

    writer = csv.writer(response)
    writer.writerow(["Name", "Email", "Phone", "Course"])

    for student in Student.objects.all():
        writer.writerow([student.name, student.email, student.phone, student.course])

    return response


@login_required
def export_courses_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="courses.csv"'

    writer = csv.writer(response)
    writer.writerow(["Course Title", "Description", "Duration"])

    for course in Course.objects.all():
        writer.writerow([course.course_title, course.description, course.duration])

    return response