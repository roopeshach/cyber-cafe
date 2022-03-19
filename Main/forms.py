from django import forms

from django.contrib.auth.models import User

from .models import UserLog, Course, TimePeriod, Student

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    def save(self):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password']
        )
        return user

#course form model
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

#time-period form model
class TimePeriodForm(forms.ModelForm):
    class Meta:
        model = TimePeriod
        fields = '__all__'

#student form model
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = [ 'status']



    
