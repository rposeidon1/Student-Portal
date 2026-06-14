from django import forms
from .models import Student, Course

INPUT_CLASSES = "w-full border border-gray-300 rounded-lg px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-400"
SELECT_CLASSES = "w-full border border-gray-300 rounded-lg px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-400 bg-white"


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email", "phone", "course"]
        widgets = {
            "name": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "email": forms.EmailInput(attrs={"class": INPUT_CLASSES}),
            "phone": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "course": forms.Select(attrs={"class": SELECT_CLASSES}),
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["course_title", "description", "duration"]
        widgets = {
            "course_title": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "description": forms.Textarea(attrs={"class": INPUT_CLASSES, "rows": 3}),
            "duration": forms.TextInput(attrs={"class": INPUT_CLASSES}),
        }