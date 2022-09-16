from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import todoform
from . models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.
class Tasklistview(ListView):
    model = Task
    template_name = 'add.html'
    context_object_name = 'task1'
class Taskdetailview(DetailView):
    model = Task
    template_name = "detailpage.html"
    context_object_name = "task"
class Taskupdateview(UpdateView):
    model = Task
    template_name = "edit.html"
    context_object_name = "task"
    fields = ("name",'prio','date')
    def get_success_url(self):
        return reverse_lazy('cvbdetail',kwargs={'pk':self.object.id})
class TaskDeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy("cbviewhome")
def add(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get("task",'')
        priority=request.POST.get("priority",'')
        date = request.POST.get("date",'')
        task = Task(name=name,prio=priority,date=date)
        task.save()
    return render(request,"add.html",{'task1': task1})
# def detail(request,id):
#
#      return render(request,"detailpage.html",{'task':task})
def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return  redirect('/')
    return  render(request,"delete.html",{'task': task})
def update(request,id):
    task = Task.objects.get(id=id)
    f = todoform(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, "update.html", {'f': f,'task': task})