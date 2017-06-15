from django.shortcuts import render

def index(request):
    print("*"*100)
    return render(request,'portfolios/index.html')

# Create your views here.
def testimonials(request):
    print("testimonials"*10)
    return render(request,'portfolios/testimonials.html')
