from django.shortcuts import render, get_object_or_404, redirect
from .models import Human
from .forms import HumanForm

def index(request):
    humans = Human.objects.all()
    selected_human = None

    if request.method == 'POST':
        selected_id = request.POST.get('selected_human')
        if selected_id:
            selected_human = get_object_or_404(Human, id=selected_id)

        if 'update' in request.POST and selected_human:
            selected_human.first_name = request.POST.get('first_name')
            selected_human.last_name = request.POST.get('last_name')
            selected_human.phone = request.POST.get('phone')
            selected_human.address = request.POST.get('address')
            selected_human.city = request.POST.get('city')
            selected_human.save()

        if 'delete' in request.POST and selected_human:
            selected_human.delete()
            return redirect('index')  # Refresh the page after deletion

    return render(request, 'index.html', {
        'humans': humans,
        'selected_human': selected_human
    })
