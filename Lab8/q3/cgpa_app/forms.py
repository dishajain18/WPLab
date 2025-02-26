from django import forms

class CGPAForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    total_marks = forms.FloatField(label='Total Marks')
