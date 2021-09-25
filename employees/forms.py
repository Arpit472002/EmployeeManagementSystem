from employees.models import EmployeeList
from django import forms
#Create your form here
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=EmployeeList
        fields=('name','age','date_of_joining','salary','picture')