from django.db import models

# Create your models here.
class Admission(models.Model):
    stu_name=models.CharField(max_length=100)
    fat_name=models.CharField(max_length=100)
    join_date=models.DateField()
    stu_class=models.CharField(max_length=100)
    fees=models.PositiveIntegerField()
def __str__(self):
    return Admission
class Meta:
    verbose_name="Admission"
    verbose_name_plural="Admissions"