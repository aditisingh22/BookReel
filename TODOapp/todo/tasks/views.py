from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.

'''
Pointer
Needs to be done so that the new app page can show the details we are quering from the database table like here tasks contains the tasks that has been added to the table and added the value in context and further passed to the template using render
'''
@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user) 
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Set the user to the logged-in user
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
    
    context = {
        'tasks': tasks,
        'form': form
    }
    return render(request, 'tasks/list.html', context)

@login_required
def updateTask(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form,
        'task': task,
    }
    return render(request, 'tasks/update_task.html', context)



def deleteTask(request,pk):
    
    item =get_object_or_404(Task , pk=pk, user=request.user)
    
    if request.method =='POST':
        item.delete()
        return redirect('/')
    context ={
            'item':item
        }
    return render(request,'tasks/delete.html',context)