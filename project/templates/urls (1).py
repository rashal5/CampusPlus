from django.urls import path
from . import views

urlpatterns = [
     
    path('',views.index, name='index'),
    path('login',views.login, name='login'),
    path('register',views.register, name='register'),
    path('signup',views.signup, name='signup'),
    path('logout',views.logout, name='register'),
    path('student',views.student, name='student'),
    path('teacher',views.teacher, name='teacher'),
    path('admin',views.admin, name='adminpage'),
    path('checkstudent',views.checkstudent, name='checkstudent'),
    path('adminp',views.adminp, name='adminp'),
    path('checkteacher',views.checkteacher, name='checkteacher'),
    path('programc',views.programc, name='programc'),
    path('registerteacher',views.registerteacher, name='registerteacher'),
    path('studenthome',views.studenthome, name='studenthome'),
    path('teacherhome',views.teacherhome, name='teacherhome'),
    path('registerstudent',views.registerstudent, name='registerstudent'),
]

