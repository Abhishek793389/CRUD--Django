from django.db import models

class EmployeeModel(models.Model):
    emp_id = models.CharField(db_column='Emp ID', unique=True, max_length=20, null=True)
    emp_name = models.CharField(db_column='Emp Name', max_length=50)
    emp_mob = models.CharField(db_column='Emp Mobile', max_length=11)
    emp_email = models.EmailField(db_column='Email', max_length=35)  
    emp_paw = models.CharField(db_column='Password', max_length=50)  
    emp_dob = models.DateField(db_column='Date of Birth')
    emp_address = models.CharField(db_column='Address', max_length=100)
    emp_dept = models.CharField(db_column='Department', max_length=30)

    class Meta:
        db_table = 'employee'

