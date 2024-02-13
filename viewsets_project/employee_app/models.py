from django.db import models


class Employee(models.Model):
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=30)
    emp_salary = models.FloatField()
    emp_designation = models.CharField(max_length=30)
    company = models.CharField(max_length=50)
