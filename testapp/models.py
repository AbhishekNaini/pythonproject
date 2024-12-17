from django.db import models
from datetime import datetime  # Correct import for datetime module

class Student(models.Model):
    name = models.CharField(max_length=50)
    student_class = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication = models.CharField(max_length=100)  # Fixed the typo 'models.models'
    year = models.PositiveIntegerField()  # Fixed the typo 'models.models'

    def __str__(self):
        return self.name


class Library(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Fixed double equal sign
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # Fixed double equal sign
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.student.name} borrowed {self.book.name}"
