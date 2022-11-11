from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'home.html')
def cscience(request):
    return render(request,'cscience.html')
def biology(request):
    return render(request,'biology.html')
def commerce(request):
    return render(request,'commerce.html')
def history(request):
    return render(request,'history.html')
def science(request):
    return render(request,'science.html')
