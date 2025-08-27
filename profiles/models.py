from django.db import models

class Profile(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_code=models.PositiveIntegerField()
def __str__(self):
    return Profile
class Meta:
    verbose_name="profile"
    verbose_name_plural="profiles"

