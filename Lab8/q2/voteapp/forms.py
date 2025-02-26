from django import forms

class VoteForm(forms.Form):
    VOTE_CHOICES = [
        ('Good', 'Good'),
        ('Satisfactory', 'Satisfactory'),
        ('Bad', 'Bad'),
    ]
    
    vote = forms.ChoiceField(choices=VOTE_CHOICES, widget=forms.RadioSelect)
