from django.contrib import admin
from .models import Profile
class ProfileAdmin(admin.ModelAdmin):
    list_display=("id","stu_name","stu_code")
admin.site.register(Profile,ProfileAdmin)


# Register your models here.
