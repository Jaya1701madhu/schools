from django.db import models

class TransportDetail(models.Model):
    
    stu_name=models.CharField(max_length=100)
    stu_route=models.CharField(max_length=100)
    stu_fees=models.PositiveIntegerField()
def __str__(self):
    return TransportDetail
class Meta:
    verbose_name="Transport"
    verbose_name_plural="Transports"
class Routedetail(models.Model):
    route_name=models.CharField(max_length=100)
    distance=models.PositiveIntegerField()
    price=models.PositiveIntegerField()
    def __str__(self):
        return Routedetail
    class Meta:
        verbose_name="Routedetail"
        verbose_name_plural="Routedetails"