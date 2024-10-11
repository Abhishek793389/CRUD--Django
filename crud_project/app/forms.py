from django import forms
from . models import EmployeeModel

class EmployeeForm(forms.ModelForm):
  class  Meta:
    model = EmployeeModel
    fields = ['emp_id', 'emp_name', 'emp_mob', 'emp_email', 'emp_paw', 'emp_dob', 'emp_address', 'emp_dept']
    labels ={'emp_id':' Employee ID',
            'emp_name': 'Employee Name',
            'emp_mob': 'Employee Mobile',
            'emp_email': 'Employee Email',
            'emp_paw': 'Employee Password',
            'emp_dob': 'Employee DOB',
            'emp_address': 'Employee Address',
            'emp_dept': 'Employee Department'
            }

    widgets ={'emp_id':forms.TextInput(attrs={'class':'form'}),
              'emp_name':forms.TextInput(attrs={'class':'form'}),
              'emp_mob':forms.TextInput(attrs={'class':'form'}),
              'emp_email':forms.EmailInput(attrs={'class':'form'}),
              'emp_paw': forms.PasswordInput(attrs={'class':'form'}),
              'emp_dob': forms.DateInput(attrs={'class':'form' ,'type':'date'}),
              'emp_address':forms.TextInput(attrs={'class':'form'}),
              'emp_dept':forms.TextInput(attrs={'class':'form'})
                }


