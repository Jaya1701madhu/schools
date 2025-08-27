from django.contrib import admin

# Register your models here.
from .models import TransportDetail
from .models import Routedetail
class TransportDetailAdmin(admin.ModelAdmin):
    list_display=("id","stu_name","stu_route","stu_fees")
admin.site.register(TransportDetail,TransportDetailAdmin)
class RoutedetailAdmin(admin.ModelAdmin):
    list_display=("id","route_name","distance","price")
admin.site.register(Routedetail,RoutedetailAdmin)
