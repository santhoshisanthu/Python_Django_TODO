from django.shortcuts import render,redirect
from .models import Task
# Create your views here.

def add(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        priority = request.POST.get('priority','')
        start_date = request.POST.get('start_date','')
        end_date = request.POST.get('end_date','')
        description = request.POST.get('description','')
        status = request.POST.get('status','')
        task = Task(name = name, priority = priority, start_date = start_date, end_date = end_date, description = description, status = status)
        task.save()
    task_list = Task.objects.all()
    return render(request, 'myapp/add.html', {'task_list': task_list})
    #return render(request,'myapp/add.html')
def home (request):
    task_list = Task.objects.all()
    return render(request, 'myapp/home.html', {'task_list': task_list})
def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    # print(id)
    return redirect('add')
def done(request, id):
    task = Task.objects.get(id=id)
    task.status = "Completed"
    task.save()
    return redirect('add')