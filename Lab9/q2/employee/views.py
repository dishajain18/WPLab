from django.shortcuts import render, redirect
from .models import Works, Lives, WorksForm
from django.http import HttpResponse

def insert_data(request):
    if request.method == 'POST':
        works_form = WorksForm(request.POST)

        if works_form.is_valid():
            # Save the data to the WORKS table
            works_entry = works_form.save()

            return HttpResponse("Data inserted successfully! Please add the 'Lives' data via the admin panel.")
        else:
            return HttpResponse("Form data is invalid.")

    else:
        works_form = WorksForm()

    return render(request, 'insert_data.html', {'works_form': works_form})


def retrieve_people(request):
    if request.method == 'POST':
        company_name = request.POST['company_name']
        people = Works.objects.filter(company_name=company_name)
        result = []

        for person in people:
            try:
                city = Lives.objects.get(person_name=person).city
                result.append(f"{person.person_name} lives in {city}")
            except Lives.DoesNotExist:
                result.append(f"{person.person_name} has no city data")

        return HttpResponse("<br>".join(result))
    
    return render(request, 'retrieve_people.html')

