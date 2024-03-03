from django.shortcuts import render

# Create your views here.

def home(request):
    name = 'prime'

    return render(request,'home.html',{
        'name': name,
    }) 

def detail(request):
    cat = ['prime','debbie']

    return render(request, 'detail.html',{
        'categories':cat,
    })