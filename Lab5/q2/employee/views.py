from django.shortcuts import render

def promotion_eligibility(request):
    return render(request, 'promotion_form.html')
