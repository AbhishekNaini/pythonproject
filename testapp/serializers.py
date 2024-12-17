from rest_framework import serializers
from .models import Student, Book, Library

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'student_class', 'photo', 'video']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'author', 'publication', 'year']

class LibrarySerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    book = BookSerializer(read_only=True)

    class Meta:
        model = Library
        fields = ['id', 'student', 'book', 'start_date', 'end_date']
