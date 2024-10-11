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


