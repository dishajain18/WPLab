from django.shortcuts import render, redirect
from .forms import CGPAForm

def input_page(request):
    if request.method == "POST":
        # Process the form data when the form is submitted
        form = CGPAForm(request.POST)
        if form.is_valid():
            # Get the cleaned data from the form
            name = form.cleaned_data['name']
            total_marks = form.cleaned_data['total_marks']

            # Calculate CGPA
            cgpa = total_marks / 50

            # Store the name and CGPA in the session
            request.session['name'] = name
            request.session['cgpa'] = cgpa

            # Redirect to the result page
            return redirect('result_page')
    else:
        form = CGPAForm()  # Create an empty form if the request is GET

    return render(request, 'input_page.html', {'form': form})


def result_page(request):
    # Retrieve the name and CGPA from the session
    name = request.session.get('name')
    cgpa = request.session.get('cgpa')

    # If no data exists in the session, redirect back to the input page
    if not name or not cgpa:
        return redirect('input_page')

    return render(request, 'result_page.html', {'name': name, 'cgpa': cgpa})
