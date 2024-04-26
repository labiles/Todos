from django.shortcuts import render, redirect
from .models import Task
from forms import Todoform
# Create your views here.

def Todo(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task':task1})

def Delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def Edit(request,id):
    task=Task.objects.get(id=id)
    form=Todoform(request.POST or None, instance=Task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'task':task},{'form':form})