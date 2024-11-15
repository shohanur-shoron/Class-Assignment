from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'addStudent.html', {'form': form, 'action': 'add'})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'studentList.html', {'students': students})

def update_student(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'addStudent.html', {'form': form, 'student': student, 'action': 'update'})

def delete_student(request, pk):
    try:
        student = Student.objects.get(pk=pk)
        student.delete()
        return redirect('student_list')
    except Student.DoesNotExist:
        return redirect('student_list')