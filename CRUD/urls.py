from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('students/create/', views.create_student, name='create_student'),
    path('students/<int:pk>/update/', views.update_student, name='update_student'),
    path('students/<int:pk>/delete/', views.delete_student, name='delete_student'),
]