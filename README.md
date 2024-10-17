# Django CRUD Project
This is a Django-based CRUD (Create, Read, Update, Delete) project designed to demonstrate the essential operations on database records, such as adding, viewing, editing, and deleting entries. This project uses MySQL as the database and provides a simple user interface with additional functionalities such as login, signup, and logout.

# you can check it by live link here :
# Live link :[https://lnkd.in/ggsWD6kN]
# Prerequisites
Ensure you have the following installed:

- Python 3.x
- Django5.1
- MySQL Database
- VS-Code

## Step 1: Create Your Project
- ***django-admin startproject 'your project name'***

  #### Then, go to your project directory.

## Step 2: Create Your App
- ***python manage.py startapp 'your appname'***

## Step 3: Install Your App in `settings.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',  # Install your app here
]
```
## Step 4: link Your `App’s URLs` to the inner Project folder `URls`
```python
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    
    
]

### Created Files in Your App: `urls.py` and `forms.py`

#### `urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.master, name='master'),
    path('show/', views.show_table, name='home'),
    path('add/', views.employee_data, name='add'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
]
```

# Create a Model for Your Database Table
`models.py`
```python
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
```
# Create a form
`forms.py`
```python
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
```
# Now write the logic of your code in `views.py`
`views.py`
```python
from django.shortcuts import render,redirect
from . forms import EmployeeForm
from . models import EmployeeModel
from django .contrib import messages


# First page Show table :

def show_table(request): 
  employees = EmployeeModel.objects.all()
  return render(request, 'app/display.html', {'emp':employees})


# Add new record to the table : 
def employee_data(request):
  if request.method == 'POST':
    form = EmployeeForm(request.POST)
    if form.is_valid():
      ei = form.cleaned_data['emp_id']
      en = form.cleaned_data['emp_name']
      em = form.cleaned_data['emp_mob']
      ee = form.cleaned_data['emp_email']
      ep = form.cleaned_data['emp_paw']
      ed = form.cleaned_data['emp_dob']
      ea = form.cleaned_data['emp_address']
      edept = form.cleaned_data['emp_dept']
      reg = EmployeeModel(emp_id=ei, emp_name=en, emp_mob=em, emp_email=ee, emp_paw=ep, emp_dob=ed, emp_address=ea, emp_dept=edept)
      reg.save() 
      messages.success(request, "User Added Successfully")
      return redirect('home')
  else:
    form = EmployeeForm()
  return render(request,'app/index.html', {'form':form})


# delete
def delete(request,id):
  if request.method =='POST':
    delete = EmployeeModel.objects.get(pk = id)
    delete.delete()
    messages.success(request, "user deleted Successfully")
    return redirect('home')
  

#Update
def update(request,id):
  if request.method == 'POST':
    update = EmployeeModel.objects.get(pk = id)
    form = EmployeeForm(request.POST, instance=update)
    if form.is_valid():
      form.save()
      messages.success(request, "Successfully Updated")
      return redirect('home')
  else:
    update = EmployeeModel.objects.get(pk=id)
    form = EmployeeForm(instance=update)
  return render(request, 'app/update.html', {'form':form})    

# master templates
def master(request):
  return render(request, 'app/master.html')
```
# setup you `static file`
```python
STATIC_DIR = BASE_DIR / 'static'

STATIC_URL = 'static/'
STATICFILES_DIRS = [STATIC_DIR,]
```
# Now for `templates` and `static` files you can checkout the direcrory of the project.
Thank You










