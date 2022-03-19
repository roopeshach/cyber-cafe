from django.shortcuts import render, redirect
from .forms import UserForm , CourseForm, TimePeriodForm, StudentForm
from .models import UserLog , Course, TimePeriod, Student
from django.views.generic.edit import UpdateView , CreateView
from django.views.generic import DetailView , ListView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
# Create your views here.
from django.contrib.auth.decorators import login_required
from django import template

register = template.Library()
@register.filter(name='subtract')
def subtract(value, arg):
    return value - arg


def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            #add user log
            
            user = User.objects.get(username=request.POST.get('username'))
            login(request, user)
            add_user_log(request.user,'Added User',request.META['REMOTE_ADDR'])
            #add user log
            return redirect('/')
        else:
            context = {
                'error' : form.errors,
            }
            return render(request, 'Main/register.html', context)
    else:
        return render(request, 'Main/register.html')


        
def login_user(request):
    if request.user.is_authenticated:
        return redirect('Main:index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                #add user log
                add_user_log(request.user,'Logged In',request.META['REMOTE_ADDR'])

                return redirect('/')
            else:
                context = {
                    'error' : 'Invalid Credentials'
                }
                return render(request, 'Main/login.html', context)
        else:  
            return render(request, 'Main/login.html')
    
#logout
def logout_user(request):
    add_user_log(request.user,'Logged Out',request.META['REMOTE_ADDR'])
    
    logout(request)
    #add user log
    return redirect('Main:login')

#function to add user log
def add_user_log(user,task, ip):
    user_log = UserLog()
    user_log.user = user
    user_log.task = task
    user_log.ip = ip
    user_log.save()

    return True


def index(request):
    if request.user.is_authenticated:
        students_count = Student.objects.all().count()
        courses_count = Course.objects.all().count()
        timeperiods_count = TimePeriod.objects.all().count()
        passed_students = Student.objects.filter(status='Passed-Out').count()
        inactive_students = Student.objects.filter(status='In-Active').count()
        started_students = Student.objects.filter(status='Started').count()
        students = Student.objects.all()[:5]
        #get time period wise student count
        timeperiod_wise_student_count = {}
        for timeperiod in TimePeriod.objects.all():
            timeperiod_wise_student_count[timeperiod.name] = Student.objects.filter(time_period=timeperiod).count()
        #get course wise student count
        course_wise_student_count = {}
        for course in Course.objects.all():
            course_wise_student_count[course.name] = Student.objects.filter(courses=course).count()
        print(course_wise_student_count)
        context = {
            'students_count' : students_count,
            'courses_count' : courses_count,
            'timeperiods_count' : timeperiods_count,
            'students' : students,
            'passed_students' : passed_students,
            'inactive_students' : inactive_students,
            'started_students' : started_students,
            'timeperiod_wise_student_count' : timeperiod_wise_student_count,
            'course_wise_student_count' : course_wise_student_count,
        }
        return render(request, 'Main/index.html', context)
    else:
        return redirect('Main:login')



class CourseView(LoginRequiredMixin , UserPassesTestMixin ,CreateView):
    def test_func(self):
        login_url = 'login/'
        return(self.request.user)

    
    def get(self,request):
        
        course_form = CourseForm()
        courses = Course.objects.all()
        context = {
            'courses': courses,
            'course_form' :course_form,
        }
        return render(request, 'Main/course.html', context)
    
    def post(self, request):
        course_form = CourseForm(request.POST , request.FILES)
        context = {
            'course_form' : CourseForm,
        }

        if course_form.is_valid():
            course_form.save()

            return redirect('Main:course')
        else:
            return render(request, 'Main/course.html', context)
  
        
        return redirect('Main:order')

@login_required
def delete_course(request , id):
    Course.objects.get(id=id).delete()
    #add user log
    add_user_log(request.user,'Deleted Order',request.META['REMOTE_ADDR'])
    return redirect('Main:course')

class UpdateCourse( LoginRequiredMixin, UpdateView):

    def test_func(self):
        login_url  = 'login/'
        return(self.request.user)
    
    model = Course

    fields = ('__all__')




class TimePeriodView(LoginRequiredMixin , UserPassesTestMixin ,CreateView):
    def test_func(self):
        login_url = 'login/'
        return(self.request.user)

    
    def get(self,request):
        
        timeperiod_form = TimePeriodForm()
        timeperiods = TimePeriod.objects.all()
        context = {
            'timeperiods': timeperiods,
            'timeperiod_form' :timeperiod_form,
        }
        return render(request, 'Main/timeperiod.html', context)
    
    def post(self, request):
        timeperiod_form = TimePeriodForm(request.POST , request.FILES)
        context = {
            'timeperiod_form' : TimePeriodForm,
        }

        if timeperiod_form.is_valid():
            timeperiod_form.save()

            return redirect('Main:timeperiod')
        else:
            return render(request, 'Main/timeperiod.html', context)
  
        
        return redirect('Main:timeperiod')

@login_required
def delete_timeperiod(request , id):
    TimePeriod.objects.get(id=id).delete()
    #add user log
    add_user_log(request.user,'Deleted Order',request.META['REMOTE_ADDR'])
    return redirect('Main:timeperiod')

class UpdateTimePeriod( LoginRequiredMixin, UpdateView):

    def test_func(self):
        login_url  = 'login/'
        return(self.request.user)
    
    model = TimePeriod

    fields = ('__all__')



class StudentView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    def test_func(self):
        login_url = 'login/'
        return(self.request.user)

    
    def get(self,request):
        
        student_form = StudentForm()
        students = Student.objects.all()
        context = {
            'students': students,
            'student_form' :student_form,
        }
        return render(request, 'Main/student.html', context)
    
    def post(self, request):
        if request.POST.get('fee'):
            student = Student.objects.get(id=request.POST.get('id'))
            fee = request.POST.get('fee')
            print(student)
            student.paid_fee += int(fee)
            student.save()
            return redirect('Main:student')
        student_form = StudentForm(request.POST , request.FILES)
        context = {
            'student_form' : StudentForm,
        }

        if student_form.is_valid():
            student_form.save()
            return redirect('Main:student')
        else:
            print(StudentForm.errors)
            return render(request, 'Main/student.html', context)
  
        
        return redirect('Main:student')

def delete_student(request , id):
    Student.objects.get(id=id).delete()
    return redirect('Main:student')

class UpdateStudent( UpdateView):

    def test_func(self):
        login_url  = 'login/'
        return(self.request.user)
    
    model = Student

    fields = ('__all__')


def toggle_student_status(request , id, status):
    student = Student.objects.get(id=id)
    student.status = status
    student.save()
    return redirect('Main:student')

