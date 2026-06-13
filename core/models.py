from django.db import models


class Course(models.Model):
    course_title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.course_title

    class Meta:
        ordering = ["course_title"]


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
