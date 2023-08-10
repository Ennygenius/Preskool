from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import *

# Create your views here.
@login_required(login_url="login")
def index(request):
    student = Student.objects.all()
    staffs = Staff.objects.all()
    classes = Class.objects.all()
    context = {
        'student':student, 
        'class': classes,
        'staffs': staffs
    }
    return render(request, 'index.html',context)


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
    return render(request, 'login.html' )


def students(request):
    students = Student.objects.all()
    paginator = Paginator(students, 3)
    page_number =  request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'students': page_obj, 
    }
    return render(request, 'students.html', context)


def add_student(request):
    if request.method == 'POST':
        form = AddStudent(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('students')
        else:
            messages.info(request, 'Credentials Invalid')
    else:
        form = AddStudent()
    return render(request, 'add-student.html', {'form': form})

def edit_student(request, id):
    students = Student.objects.get(pk=id)
    if request.method == 'POST':
        form = AddStudent(request.POST,  request.FILES, instance=students)
        if form.is_valid():
            form.save()
            return redirect('students')
        else:
            messages.info(request, 'Credentials Invalid')
    else:
        form = AddStudent(instance=students)
    return render(request, 'edit-student.html', {'form': form})
   
def student_details(request,id):
    student = Student.objects.get(pk=id)
    context = {
        'students': student
    }
    return render(request, 'student-details.html', context)

def delete_student(request, id):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect('students')

def teachers(request):
    staffs = Staff.objects.all()
    context={
        'staffs': staffs
    }
    return render(request, 'teachers.html', context)

def add_teachers(request):
    if request.method == 'POST':
        form = AddStaff(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teachers')
    else:
        form = AddStaff()
    return render(request, 'add-teacher.html', {'form': form})

def edit_staff(request, id):
    staffs = Staff.objects.get(pk=id)
    if request.method == 'POST':
        form = AddStaff(request.POST,  request.FILES, instance=staffs)
        if form.is_valid():
            form.save()
            return redirect('teachers')
        else:
            messages.info(request, 'Credentials Invalid')
    else:
        form = AddStudent(instance=staffs)
    return render(request, 'edit-teacher.html', {'form': form})

def delete_staff(request, id):
    staff = Staff.objects.get(pk=id)
    staff.delete()
    return redirect('teachers')

def logout_view(request):
    logout(request)
    return redirect('/')