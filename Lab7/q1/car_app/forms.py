from django import forms

class CarForm(forms.Form):
    manufacturers = [
        ('Toyota', 'Toyota'),
        ('Ford', 'Ford'),
        ('BMW', 'BMW'),
        ('Honda', 'Honda'),
        ('Chevrolet', 'Chevrolet'),
    ]
    manufacturer = forms.ChoiceField(choices=manufacturers, label='Select Car Manufacturer')
    model = forms.CharField(max_length=100, label='Model Name')
