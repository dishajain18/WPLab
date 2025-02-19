from django.shortcuts import render, redirect
from .forms import UserForm

def first_page(request):
    # If there's a session with values, fill the form with those values i.e in case we come to first page from second page retain those values
    initial_data = {
        'name': request.session.get('name', ''),
        'roll': request.session.get('roll', ''),
        'subject': request.session.get('subject', '')
    }

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Get the form data
            name = form.cleaned_data['name']
            roll = form.cleaned_data['roll']
            subject = form.cleaned_data['subject']

            # Store the form data in the session
            request.session['name'] = name
            request.session['roll'] = roll
            request.session['subject'] = subject

            # Redirect to the second page
            return redirect('second_page')
    else:
        # Pre-populate the form with initial data from session
        form = UserForm(initial=initial_data)

    return render(request, 'firstPage.html', {'form': form})

def second_page(request):
    # Retrieve data from the session
    name = request.session.get('name', 'Not Provided')
    roll = request.session.get('roll', 'Not Provided')
    subject = request.session.get('subject', 'Not Selected')

    # Render the second page with the data
    return render(request, 'secondPage.html', {
        'name': name,
        'roll': roll,
        'subject': subject
    })
