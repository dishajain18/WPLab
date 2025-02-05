from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    address = forms.CharField(widget=forms.Textarea)
    contact_number = forms.CharField(max_length=15)
    email = forms.EmailField()
    english_marks = forms.IntegerField(min_value=0, max_value=100)
    physics_marks = forms.IntegerField(min_value=0, max_value=100)
    chemistry_marks = forms.IntegerField(min_value=0, max_value=100)
