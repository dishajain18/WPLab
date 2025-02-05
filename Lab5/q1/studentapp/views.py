from django.shortcuts import render

def student_form(request):
    return render(request, 'student_form.html')
