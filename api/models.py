from django.db import models

# Create your models here.
class employees(models.Model):
    EmployeeName=models.CharField(max_length=100)
    Address=models.CharField(max_length=150)
    EmployeeID=models.IntegerField(max_length=10)

def _str_(self):
    return self.EmployeeName