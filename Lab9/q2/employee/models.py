from django.db import models
from django import forms

# Model definitions
class Works(models.Model):
    person_name = models.CharField(primary_key=True, max_length=100)
    company_name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.person_name


class Lives(models.Model):
    person_name = models.OneToOneField(Works, on_delete=models.CASCADE, primary_key=True)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.person_name.person_name


# ModelForm for Works (since Lives is to be populated only by admin)
class WorksForm(forms.ModelForm):
    class Meta:
        model = Works
        fields = ['person_name', 'company_name', 'salary']
