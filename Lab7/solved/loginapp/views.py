from django.shortcuts import render
from loginapp.forms import LoginForm

def login(request): 
    username = "not logged in" 
    cn = "not found"
    MyLoginForm = LoginForm()  # Initialize form by default

    if request.method == "POST":
        # Get the posted form
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username'] 
            cn = MyLoginForm.cleaned_data['contact_num']
            # After login success, render loggedin.html
            return render(request, 'loggedin.html', {'username': username, 'contact_num': cn})
    
    # For GET request, render login.html
    return render(request, 'login.html', {'form': MyLoginForm})
