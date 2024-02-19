from django.urls import path
from . import views
from .views import view_profile
from .views import view_profile1
from .views import get_filtered_courses

urlpatterns = [
    path('profile/', view_profile, name='view_profile'), 
    path('profile1/', view_profile1, name='view_profile1'), 
    path('',views.index, name='index'),
    path('login',views.login, name='login'),
    path('register',views.register, name='register'),
    path('signup',views.signup, name='signup'),
    path('logout',views.logout, name='register'),
    path('student',views.student, name='studentpage'),
    path('teacher',views.teacher, name='teacherpage'),
    path('admin',views.admin, name='adminpage'),
    path('registerstudent',views.registerstudent, name='registerstudent'),
    path('registerteacher',views.registerteacher, name='registerteacher'),
    path('registeradmin',views.registeradmin, name='registeradmin'),
    path('home',views.home, name='home'),
    path('studenthome',views.studenthome, name='studenthome'),
    path('teacherhome',views.teacherhome, name='teacherhome'),
    path('checkstudent',views.checkstudent, name='checkstudent'),
    path('adminp',views.adminp, name='adminp'),
    path('checkteacher',views.checkteacher, name='checkteacher'),
    path('cos',views.cos, name='cos'),
    path('create_department',views.create_department, name='create_department'),
    path('create_course',views.create_course, name='create_course'),
    path('upload_pdf/', views.upload_pdf, name='upload_pdf'),
    path('pdf_list/<int:pm>/', views.pdf_list, name='pdf_list'),
    path('download_pdf/<int:pdf_id>/', views.download_pdf, name='download_pdf'),
    path('dep/', views.dep, name='dep'),
    path('coss/<int:pk>/', views.coss, name='coss'),
    path('addprogram',views.addprogram, name='addprogram'),
    path('viewstudent',views.viewstudent, name='viewstudent'),
    path('pdfview',views.pdfview, name='pdfview'),
    path('delpdf/<int:pk>/',views.delpdf, name='delpdf'),
    path('feedbackstudent',views.feedbackstudent, name='feedbackstudent'),
    path('viewfeedback',views.viewfeedback, name='viewfeedback'),
    path('fillform',views.fillform, name='fillform'),
    path('already_submitted',views.already_submitted, name='already_submitted'),
    path('notfilled',views.notfilled, name='notfilled'),
    path('get_filtered_courses/', get_filtered_courses, name='get_filtered_courses'),
    path('feedbackteacher',views.feedbackteacher, name='feedbackteacher'),
    path('viewfeedbacks',views.viewfeedbacks, name='viewfeedbacks'),
    path('addnotification',views.addnotification, name='addnotification'),
    path('students_list', views.student_list, name='student_list'),
    path('teachers_list', views.teacher_list, name='teacher_list'),
    path('deleteitem', views.deleteitem, name='deleteitem'),
    path('delitem/<int:pk>/', views.delitem, name='delitem'),
    
    
]



