from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('studentslist', views.students_list, name="students_list"),
]
