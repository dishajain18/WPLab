from django import forms

class UserForm(forms.Form):
    subjects = [
        ('Math', 'Math'),
        ('Physics', 'Physics'),
        ('Chemistry', 'Chemistry'),
        ('Biology', 'Biology'),
    ]
    name = forms.CharField(max_length=100, label="Name")
    roll = forms.CharField(max_length=100, label="Roll Number")
    subject = forms.ChoiceField(choices=subjects, label="Select Subject")
