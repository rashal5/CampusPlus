from django.contrib import admin
from app.models import Notification,Fillfrom,User,Code,Department,Course,PDFDocument,Memo,UserProfile,Feedback
# Register your models here.
admin.site.register(User)
admin.site.register(Code)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(PDFDocument)
admin.site .register(Memo)
admin.site .register(UserProfile)
admin.site.register(Feedback)
admin.site.register(Fillfrom)
admin.site.register(Notification)
