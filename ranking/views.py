from django.shortcuts import render, get_object_or_404
from .models import Film, Review

def film(request, pk):
    film = get_object_or_404(Film, pk=pk)
    return render(request, 'ranking/film.html', {'film': film})
    
def review_list(request):
    reviews_phoebe = Review.objects.filter(author='phoebe').order_by('date')
    reviews_jon = Review.objects.filter(author='jon').order_by('date')
    return render(request, 'ranking/review_list.html', 
                  {'reviews_phoebe': reviews_phoebe,
                   'reviews_jon': reviews_jon})
