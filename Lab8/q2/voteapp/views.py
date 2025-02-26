from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import VoteForm

def vote_view(request):
    # Initialize votes in session if not already present
    if 'votes' not in request.session:
        request.session['votes'] = {'Good': 0, 'Satisfactory': 0, 'Bad': 0}
    
    if request.method == "POST":
        form = VoteForm(request.POST)
        if form.is_valid():
            vote = form.cleaned_data['vote']
            
            # Increment the vote count in the session
            request.session['votes'][vote] += 1
            request.session.modified = True  # Mark the session as modified to save it
    
    else:
        form = VoteForm()  # Initialize an empty form when the page is first loaded
    
    # Calculate percentages based on the votes in the session
    total_votes = sum(request.session['votes'].values())
    percentages = {}
    
    if total_votes > 0:
        for choice, count in request.session['votes'].items():
            percentages[choice] = (count / total_votes) * 100
    else:
        percentages = {choice: 0 for choice in request.session['votes']}
    
    return render(request, 'vote.html', {
        'form': form, 
        'votes': request.session['votes'], 
        'percentages': percentages
    })
