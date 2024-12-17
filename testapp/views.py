
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Book, Library
from .forms import StudentForm, BookForm, LibraryForm


# Student Views
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'create_student.html', {'form': form})

def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form})


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'confirm_delete.html', {'object': student})


# Book Views
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'confirm_delete.html', {'object': book})



# Library Views
def library_list(request):
    libraries = Library.objects.select_related('student', 'book').all()
    return render(request, 'library_list.html', {'libraries': libraries})

def issue_book(request):
    if request.method == 'POST':
        form = LibraryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('library_list')
    else:
        form = LibraryForm()
    return render(request, 'issue_book.html', {'form': form})

def edit_issue(request, pk):
    issue = get_object_or_404(Library, pk=pk)
    if request.method == 'POST':
        form = LibraryForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect('library_list')
    else:
        form = LibraryForm(instance=issue)
    return render(request, 'edit_issue.html', {'form': form})

def delete_issue(request, pk):
    issue = get_object_or_404(Library, pk=pk)
    if request.method == 'POST':
        issue.delete()
        return redirect('library_list')
    return render(request, 'confirm_delete.html', {'object': issue})

from rest_framework import viewsets
from .models import Student, Book, Library
from .serializers import StudentSerializer, BookSerializer, LibrarySerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

