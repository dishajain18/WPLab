from django import forms

GROCERY_CHOICES = [
    ("Wheat", "Wheat"),
    ("Jaggery", "Jaggery"),
    ("Dal", "Dal"),
]

ITEM_PRICES = {
    "Wheat": 40,
    "Jaggery": 60,
    "Dal": 80,
}

class GroceryForm(forms.Form):
    items = forms.MultipleChoiceField(
        choices=GROCERY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
