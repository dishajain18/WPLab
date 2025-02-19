from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CarForm

def car_form(request):
    # Handle form submission
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            manufacturer = form.cleaned_data['manufacturer']
            model = form.cleaned_data['model']
            
            # Store the data in session
            request.session['manufacturer'] = manufacturer
            request.session['model'] = model
            
            # Redirect to the result page
            return redirect('result')
    else:
        form = CarForm()
    
    return render(request, 'car_form.html', {'form': form})

def car_result(request):
    # Retrieve data from session
    manufacturer = request.session.get('manufacturer', 'Not Selected')
    model = request.session.get('model', 'Not Provided')
    
    return render(request, 'car_result.html', {'manufacturer': manufacturer, 'model': model})

