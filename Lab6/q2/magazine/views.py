from django.shortcuts import render

def index(request):
    return render(request, 'magazine.html')
# Create your views here.
