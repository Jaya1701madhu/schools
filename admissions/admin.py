from django.contrib import admin
from .models import Admission
class AdmisssionAdmin(admin.ModelAdmin):
    list_display=("id","stu_name","fat_name","join_date","stu_class","fees")
admin.site.register(Admission,AdmisssionAdmin)

