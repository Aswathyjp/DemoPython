from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from . models import movie
from . form import mform


def home(request):
    movieobj = movie.objects.all()
    context ={
        'movie_list': movieobj
                }
    return render(request,'index.html',context)
def detail(request,movie_id):
    Movie = movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'Movie':Movie})
def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        Movie= movie(name=name,desc=desc,year=year,img=img)
        Movie.save()

    return render(request,'add.html')
def update(request,movie_id):
    Movie = movie.objects.get(id=movie_id)
    form = mform(request.POST or None,request.FILES,instance=Movie)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'edit.html',{'form':form,'movie':Movie})
def delete(request,movie_id):
    if request.method == 'POST':
        Movie = movie.objects.get(id=movie_id)
        Movie.delete()
        return redirect('/')
    return  render(request,'delete.html')
