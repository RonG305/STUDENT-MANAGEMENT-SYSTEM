from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from students.forms import StudentForm
from students.models import Student


# Create your views here.

def index(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'students/index.html', context)
   

def create_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  
    context = {
        'form':form
    }
    return render(request, 'students/create_student.html', context)


def update_student(request,pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'students/update.html', context)

def delete_student(request,pk):
    student = Student.objects.get(id=pk)
    context = {
        'student': student
    }
    student.delete()
    return render(request, 'students/delete.html', context)    






