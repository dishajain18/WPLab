from django.shortcuts import render

def index(request):
    return render(request,'calculator.html')
# Create your views here.
