from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.shortcuts import render, redirect
from .forms import SignUpForm,LoginForm,SignUpFormstudent,SignUpFormteacher,CodeForm,SignUpFormadmin,DepartmentForm, CourseForm
from .models import Code,Department,Course,Memo,Fillfrom
from django.contrib import messages
from django.http import FileResponse
from .models import PDFDocument
from .forms import PDFDocumentForm,ProgramsForm,FilloutForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile,Feedback,Feedbacks
from .forms import UserProfileForm,UserFeedbackForm,UserFeedbackForms,ProgramForm
from .models import Course,Notification
from django.shortcuts import render
from django.contrib.auth import get_user_model

# views.py
from django.http import JsonResponse

def get_filtered_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).values('id', 'name')
    data = list(courses)
    return JsonResponse({'courses': data})







@login_required
def view_profile(request):
    # Assuming there is a UserProfile instance for the current user
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'profile.html', {'form': form, 'profile': profile})

@login_required
def view_profile1(request):
    # Assuming there is a UserProfile instance for the current user
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile1')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'profile1.html', {'form': form, 'profile': profile})


# Create your views here.


def index(request):

    return render(request,'index.html')
def home(request):
    return render(request, 'home.html')
def studenthome(request):
    return render(request, 'studenthome.html')
def teacherhome(request):
    return render(request, 'teacherhome.html')
def register(request):
    msg= None
    if request.method == 'POST':
       form = SignUpForm(request.POST)
       if form.is_valid():
           user = form.save()
           msg ='uesr created'
           return redirect('login')
       else:
           msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'register.html',{'form':form,'msg':msg})


def login(request):
    msg = None
    if request.method == 'POST':
           username = request.POST['username']
           password = request.POST['password']
           user = authenticate(username=username, password=password)
           if user is not None and user.is_admin:
               auth.login(request,user)
               return redirect('adminpage')
           elif user is not None and user.is_student:
               auth.login(request,user)
               return redirect('checkstudent')
           elif user is not None and user.is_teacher:
               auth.login(request,user)
               return redirect('checkteacher')
           else:
               msg = 'invalid '
    else:
           msg = ' '    
    return render(request, 'login.html',{'msg':msg})
def admin(request):
    return render(request,"admin.html")
def student(request):
    progarms= Memo.objects.all()
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    fillform, created = Fillfrom.objects.get_or_create(user=request.user)
    note = Notification.objects.all()
    

    return render(request,"student.html",{'programs':progarms, 'profile': profile,'fillform': fillform,'note':note})
def teacher(request):
    progarms= Memo.objects.all()
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request,"teacher.html",{'programs':progarms, 'profile': profile})

def logout(request):
    auth.logout(request)
    return redirect('login')

def signup(request):
    (request)
    return redirect('signup')

def registerstudent(request):
    msg= None
    if request.method == 'POST':
       form = SignUpFormstudent(request.POST)
       if form.is_valid():
           user = form.save()
           msg ='uesr created'
           return redirect('login')
       else:
           msg = 'form is not valid'
    else:
        form = SignUpFormstudent()
    return render(request, 'registerstudent.html',{'form':form,'msg':msg})

def registerteacher(request):
    msg= None
    if request.method == 'POST':
       form = SignUpFormteacher(request.POST)
       if form.is_valid():
           user = form.save()
           msg ='uesr created'
           return redirect('login')
       else:
           msg = 'form is not valid'
    else:
        form = SignUpFormteacher()
    return render(request, 'registerteacher.html',{'form':form,'msg':msg})

def registeradmin(request):
    msg= None
    if request.method == 'POST':
       form = SignUpFormadmin(request.POST)
       if form.is_valid():
           user = form.save()
           msg ='uesr created'
           return redirect('login')
       else:
           msg = 'form is not valid'
    else:
        form = SignUpFormadmin()
    return render(request, 'registeradmin.html',{'form':form,'msg':msg})

def checkstudent(request):
    if request.method =='POST':
        codes = request.POST['codes']
        records = Code.objects.filter(studentcode=codes)

        if records.exists():
                 return redirect('studentpage')
        else:
                messages.info(request,'invalid key. please contact college administration to get the key')
                return redirect('checkstudent')     
    else:
     return render(request, 'checkstudent.html')


def checkteacher(request):
    if request.method =='POST':
        codes = request.POST['codes']
        records = Code.objects.filter(teachercode=codes)

        if records.exists():
                 return redirect('teacherpage')
        else:
                messages.info(request,'invalid key. please contact college administration to get the key')
                return redirect('checkteacher')     
    else:
     return render(request, 'checkteacher.html')
    
def adminp(request):
    if request.method =='POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminpage')
    else:
         form= CodeForm()
    return render(request, 'adminp.html', {'form': form})


def create_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminpage')
    else:
        form = DepartmentForm()
    return render(request, 'department_form.html', {'form': form})

def create_course(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacherpage')
    else:
        form = CourseForm()
    return render(request, 'course_form.html', {'form': form,'profile': profile})

def cos(request):
    courses=Department.objects.all()
    return render(request, 'cos.html',{'courses':courses})



def upload_pdf(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = PDFDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teacherpage')
    else:
        form = PDFDocumentForm()
    return render(request, 'upload_pdf.html', {'form': form,'profile': profile})


def pdf_list(request,pm):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    pdf_documents = PDFDocument.objects.filter(course_id=pm)
    return render(request, 'pdf_list.html', {'pdf_documents': pdf_documents,'profile': profile})



def download_pdf(request, pdf_id):
    pdf_document = PDFDocument.objects.get(pk=pdf_id)
    pdf_path = pdf_document.pdf_file.path

    response = FileResponse(open(pdf_path, 'rb'))
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = f'attachment; filename="{pdf_document.title}.pdf"'
    return response



def dep(request):
    fillform, created = Fillfrom.objects.get_or_create(user=request.user)
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if fillform.submitted:
        current_user = request.user

        user_choice = Fillfrom.objects.get(user=current_user)
        chosen_model = user_choice.department
        filtered_items = Department.objects.filter(name=chosen_model.name)
        # You can pass the filtered queryset to the template or perform any other operations
        return render(request, 'dep.html', {'filtered_items': filtered_items,'profile': profile,'fillform':fillform})
    else:
        # Handle the case when the user hasn't made a choice yet
          return render(request, 'notfilled.html',{'profile': profile})

def notfilled(request):
    return render(request, 'notfilled.html')  
       

def depp(request):
    deps=Department.objects.filter()
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'dep.html',{'deps':deps, 'profile': profile})


def coss(request,pk):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    current_user = request.user
    user_choice = Fillfrom.objects.get(user=current_user)
    chosen_model = user_choice.course
    filtered_items = Course.objects.filter(name=chosen_model.name)
    cop=Course.objects.filter(department_id=pk)
    return render(request, 'coss.html',{'filtered_items':filtered_items,'profile':profile})


def addprogram(request):
    if request.method == 'POST':
        form = ProgramsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminpage')
    else:
        form = ProgramsForm()
    return render(request, 'addprogram.html', {'form': form})

def addnotification(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacherpage')
    else:
        form = ProgramForm()
    return render(request, 'addnotification.html', {'form': form,'profile': profile})







def viewstudent(request):
    students = Fillfrom.objects.all()
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request,"viewstudent.html",{'students':students,'profile':profile})

def feedbackstudent(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method =='POST':
        form = UserFeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.submitter = request.user
            form.save()
            return redirect('studentpage')
    else:
         form= UserFeedbackForm()
    return render(request, 'feedbackstudent.html', {'form': form,'profile': profile})

def viewfeedback(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    feed = Feedback.objects.all()
    return render(request,"viewfeedback.html",{'feed':feed,'profile':profile})
def feedbackteacher(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method =='POST':
        form = UserFeedbackForms(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.submitter = request.user
            form.save()
            return redirect('teacherpage')
    else:
         form= UserFeedbackForms()
    return render(request, 'feedbackteacher.html', {'form': form,'profile': profile})

def viewfeedbacks(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    feed = Feedbacks.objects.all()
    return render(request,"viewfeedbacks.html",{'feed':feed,'profile':profile})



@login_required
def fillform(request):
    fillform, created = Fillfrom.objects.get_or_create(user=request.user)
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if fillform.submitted:  # Check if the form has already been submitted
        return render(request, 'already_submitted.html',{'profile': profile})  # Create this template with an appropriate message

    if request.method == 'POST':
        form = FilloutForm(request.POST, instance=fillform)
        if form.is_valid(): 
            form.save()
            fillform.submitted = True  # Mark the form as submitted
            fillform.save()
            return redirect('studentpage')
    else:
        form = FilloutForm(instance=fillform)

    return render(request, 'fillform.html', {'form': form, 'fillform': fillform,'profile': profile})


def already_submitted(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request,"already_submitted.html",{'profile': profile})

def student_list(request):
    User = get_user_model()
    students = User.objects.filter(is_student=True)
    return render(request, 'student_list.html', {'students': students})

def teacher_list(request):
    User = get_user_model()
    teachers = User.objects.filter(is_teacher=True)
    return render(request, 'teacher_list.html', {'teachers': teachers})


def deleteitem(request):
     
     codes= Code.objects.all()
     memos = Memo.objects.all()
     departments = Department.objects.all()

     return render(request,'deleteitem.html',{'codes':codes,'memos':memos,'departments':departments})


def delitem(request,pk): 
    Code.objects.filter(id=pk).delete()
    Memo.objects.filter(id=pk).delete()
    Department.objects.filter(id=pk).delete()
    return render(request,'delitem.html')



def pdfview(request):
     profile, created = UserProfile.objects.get_or_create(user=request.user)
     views= PDFDocument.objects.all()
     courses= Course.objects.all()
     notifications= Notification.objects.all()
     return render(request,'pdfview.html',{'views':views,'courses':courses,'notifications':notifications,'profile':profile})

def delpdf(request,pk): 
    PDFDocument.objects.filter(id=pk).delete()
    Course.objects.filter(id=pk).delete()
    Notification.objects.filter(id=pk).delete()
    return render(request,'delpdf.html')


# views.py



