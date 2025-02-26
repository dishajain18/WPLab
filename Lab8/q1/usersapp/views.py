from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm

# Register Page View
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Get form data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            contact = form.cleaned_data['contact']

            # Save data in session
            request.session['username'] = username
            request.session['password'] = password
            request.session['email'] = email
            request.session['contact'] = contact

            # Redirect to Success page
            return redirect('success')
        else:
            # If form is invalid, display error messages
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

# Success Page View
def success_view(request):
    username = request.session.get('username')
    email = request.session.get('email')
    contact = request.session.get('contact')

    if username:
        return render(request, 'success.html', {
            'username': username,
            'email': email,
            'contact': contact,
        })
    else:
        return redirect('register')
