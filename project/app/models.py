from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class Code(models.Model):
    studentcode=models.CharField(max_length=10)
    teachercode=models.CharField(max_length=10)

    def __str__(self):
        return self.studentcode
    def __str__(self):
        return self.teachercode
    
class Department(models.Model):
    name = models.CharField(max_length=100)
    description=models.CharField(max_length=300)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    description1=models.CharField(max_length=300)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class PDFDocument(models.Model):
    course_name = models.CharField(max_length=255,blank=True)
    title = models.CharField(max_length=255,blank=True)
    pdf_file = models.FileField(upload_to='pdf_document/',blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    explain= models.CharField(max_length=900, blank=True)
    link =models.CharField(max_length=300, blank=True)
    link_topic =models.CharField(max_length=100, blank=True)
    

    def __str__(self):
        return self.title
    

class Memo(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
    def __str__(self):
        return self.description
class Notification(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
    def __str__(self):
        return self.description
    

class Feedback(models.Model):
    submitter  = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=500)

    def __str__(self):
        return self.feedback
    def __str__(self):
        return f"{self.submitter.username}'s feedback"
class Feedbacks(models.Model):
    submitter  = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=500)

    def __str__(self):
        return self.feedback
    def __str__(self):
        return f"{self.submitter.username}'s feedbacks"

class Fillfrom(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    guardian_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=10)
    email = models.EmailField()
    department = department = models.ForeignKey(Department,null=True, blank=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Course,null=True, blank=True, on_delete=models.CASCADE)
    submitted = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username













    

