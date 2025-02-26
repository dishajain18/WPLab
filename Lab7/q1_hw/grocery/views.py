from django.shortcuts import render
from .forms import GroceryForm, ITEM_PRICES

def grocery_view(request):
    selected_items = []
    
    if request.method == "POST":
        form = GroceryForm(request.POST)
        if form.is_valid():
            selected_items = [
                (item, ITEM_PRICES[item]) for item in form.cleaned_data['items']
            ]
    else:
        form = GroceryForm()

    return render(request, "grocery_list.html", {"form": form, "selected_items": selected_items})
