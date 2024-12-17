from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [
    # Student URLs
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.create_student, name='create_student'),
    path('students/edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:pk>/', views.delete_student, name='delete_student'),

    # Book URLs
    path('books/', views.book_list, name='book_list'),
    path('books/create/', views.create_book, name='create_book'),
    path('books/edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),

    # Library URLs
    path('library/', views.library_list, name='library_list'),
    path('library/issue/', views.issue_book, name='issue_book'),
    path('library/edit/<int:pk>/', views.edit_issue, name='edit_issue'),
    path('library/delete/<int:pk>/', views.delete_issue, name='delete_issue'),
]

router = DefaultRouter()
router.register(r'students', views.StudentViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'library', views.LibraryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]