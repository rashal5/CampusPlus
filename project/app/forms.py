from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import  Notification,Feedbacks,Fillfrom,User,Code,Department,Course,PDFDocument,Memo,UserProfile,Feedback


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email', 'profile_picture']

    email = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    profile_picture = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"class": "form-control-file"})
    )

class LoginForm(forms.Form):
    username= forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-contorl"
            }
        )
    )
    password= forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-contorl"
            }
        )
    )

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input100"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "input100"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "input100"})
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input100"})
    )

    is_student = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    is_teacher = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))

    def clean(self):
        cleaned_data = super().clean()
        is_student = cleaned_data.get('is_student')
        is_teacher = cleaned_data.get('is_teacher')

        if is_student and is_teacher:
            raise forms.ValidationError("Please select either Student or Teacher, not both.")

        if not is_student and not is_teacher:
            raise forms.ValidationError("Please select either Student or Teacher.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_student', 'is_teacher')


class SignUpFormstudent(UserCreationForm):
    username= forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"input100"
            }
        )
    )
    password1= forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"input100"
            }
        )
    )
    password2= forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"input100"
            }
        )
    )
    email= forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"input100"
            }
        )
    )

    class Meta:
        model=User
        fields = ('username','email','password1','password2','is_student') 

class SignUpFormteacher(UserCreationForm):
    username= forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"input100"
            }
        )
    )
    password1= forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"input100"
            }
        )
    )
    password2= forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"input100"
            }
        )
    )
    email= forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"input100"
            }
        )
    )

    class Meta:
        model=User
        fields = ('username','email','password1','password2','is_teacher')    

class CodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = ['studentcode','teachercode']


class SignUpFormadmin(UserCreationForm):
    username= forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-contorl"
            }
        )
    )
    password1= forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-contorl"
            }
        )
    )
    password2= forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-contorl"
            }
        )
    )
    email= forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-contorl"
            }
        )
    )

    class Meta:
        model=User
        fields = ('username','email','password1','password2','is_admin')  


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name','description']
        

class CourseForm(forms.ModelForm):
    name= forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"input100"
            }
        )
    )
    department= forms.ModelChoiceField(
        queryset=Department.objects.all(),
        widget=forms.Select(attrs={"class": "input100"})
    )
    description1= forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"input100"
            }
        )
    )
    class Meta:
        model = Course
        fields = ['name', 'department','description1']




class PDFDocumentForm(forms.ModelForm):
    course_name= forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"input100"
            }
        ),
    required=False
    )
    title= forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"input100"
            }
        ),
    required=False
    )
    course= forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=forms.Select(attrs={"class": "input100"})
    )
    explain= forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"input100"
            }
        ),
    required=False
    )
    link_topic= forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"input100"
            }
        ),
    required=False
    )
    link= forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"input100"
            }
        ),
    required=False
    )

    class Meta:
        model = PDFDocument
        fields = ['course_name','title', 'pdf_file','course','explain','link_topic','link']

class ProgramsForm(forms.ModelForm):
    title= forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"input100"
            }
        )
    )
    description= forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"input100"
            }
        )
    )
    class Meta:
        model = Memo
        fields = ['title','description']
class ProgramForm(forms.ModelForm):
    title= forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"input100"
            }
        )
    )
    description= forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"input100"
            }
        )
    )
    class Meta:
        model = Notification
        fields = ['title','description']



class UserFeedbackForm(forms.ModelForm):
    feedback= forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"input100"
            }
        )
    )
    class Meta:
        model = Feedback
        fields = ['feedback']

        feedback= forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-contorl"
            }
        )
    )
class UserFeedbackForms(forms.ModelForm):
    feedback= forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"input100"
            }
        )
    )
    class Meta:
        model = Feedbacks
        fields = ['feedback']

        feedback= forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-contorl"
            }
        )
    )
        

class FilloutForm(forms.ModelForm):
    full_name= forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"input100"
            }
        )
    )
    guardian_name= forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"input100"
            }
        )
    )
    contact_number= forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "class":"input100"
            }
        )
    )
    email= forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"input100"
            }
        )
    )
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "input100"
            }
        )
    )
    course = forms.ModelChoiceField(
        queryset=Course.objects.filter(),
        widget=forms.Select(
            attrs={
                "class": "input100"
            }
        )
    )
    class Meta:
        model = Fillfrom
        fields = ['full_name','guardian_name','contact_number','email','department','course']