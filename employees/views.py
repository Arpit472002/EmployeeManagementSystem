from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from employees.forms import EmployeeForm
from employees.models import EmployeeList
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/login')
def home(request):
    if request.method=='GET':
        form=EmployeeForm()
        list=EmployeeList.objects.all()
        return render(request,'home.html',{'form':form,'list':list})
    if request.method=='POST':
        form=EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        list=EmployeeList.objects.all()
        return HttpResponseRedirect('/home')

@login_required(login_url='/login')
def delete(request,id):
    if request.method=='POST':
        x=EmployeeList.objects.get(id=id)
        x.delete()
        return HttpResponseRedirect('/home')
    return HttpResponse("Item not deleted")

@login_required(login_url='/login')
def update(request,id):
    if request.method=='GET':
        x=EmployeeList.objects.get(id=id)
        form=EmployeeForm(instance=x)
        return render(request,'update.html',{'form':form})
    if request.method=='POST':
        x=EmployeeList.objects.get(id=id)
        form=EmployeeForm(request.POST,request.FILES,instance=x)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/home')