from django.urls import path
from . import views

urlpatterns = [
    path('search', views.search, name="search"),
    path('addbooks', views.add_books, name="addbooks"),
    path('issuebooks', views.issue_books, name="issuebooks"),
    path('viewissuebooks', views.issue_books_view, name="viewissuebooks"),
    path('returnbooks/<int:id>', views.return_book, name="return_books"),
    path('studentissue', views.student_issuedbooks, name="studentissue")
]
