from django.db import models
from django.shortcuts import reverse
# Create your models here.

class UserLog(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    ip = models.CharField(max_length=200,blank=True , null=True)
    task = models.CharField(max_length=200)
    added_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse("Main:index")

#course model
class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    fee = models.IntegerField(default=0)
    added_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("Main:course")

#time-period model
class TimePeriod(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("Main:timeperiod")

#student model
class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    added_on = models.DateTimeField(auto_now_add=True)
    courses = models.ManyToManyField(Course)
    joined_date = models.CharField(max_length=200,blank=True , null=True)
    address = models.TextField(blank=True , null=True)
    total_fee = models.IntegerField(default=0)
    paid_fee = models.IntegerField(default=0)


    status = models.CharField(max_length=200, default='Pending', blank=True, null=True)
    time_period = models.ForeignKey(TimePeriod, on_delete=models.CASCADE)
    remarks = models.TextField(blank=True , null=True)
    
    def get_paid_fee(self):
        return self.paid_fee

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("Main:student")
