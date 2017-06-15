from django.shortcuts import render

def index(request):
    print ("Index" * 10)
    return render(request,'r_portfolio/index.html')

def projects(request):
    return render(request,'r_portfolio/projects.html')

def about(request):
    return render(request,'r_portfolio/about.html')

def testimonials(request):
    return render(request,'r_portfolio/testimonials.html')

# Create your views here.
