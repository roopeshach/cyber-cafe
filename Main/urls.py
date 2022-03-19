from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register_user, name='register'),
    path('login' , views.login_user, name='login'),
    path('logout' , views.logout_user, name='logout'),


    path('course' , views.CourseView.as_view() , name='course'),
    path('update-course/<int:pk>', views.UpdateCourse.as_view(), name="update-course"),
    path('delete-course/<int:id>', views.delete_course, name="delete-course"),

     path('timeperiod' , views.TimePeriodView.as_view() , name='timeperiod'),
    path('update-timeperiod/<int:pk>', views.UpdateTimePeriod.as_view(), name="update-timeperiod"),
    path('delete-timeperiod/<int:id>', views.delete_timeperiod, name="delete-timeperiod"),

     path('student' , views.StudentView.as_view() , name='student'),
    path('update-student/<int:pk>', views.UpdateStudent.as_view(), name="update-student"),
    path('delete-student/<int:id>', views.delete_student, name="delete-student"),
    path('toggle-student-status/<int:id>/<str:status>', views.toggle_student_status, name="toggle-student-status"),
    
]
