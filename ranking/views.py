from django.shortcuts import render, get_object_or_404
from .models import Film, Review

def film(request, pk):
    film = get_object_or_404(Film, pk=pk)
    return render(request, 'ranking/film.html', {'film': film})
    
def review_list(request):
    reviews = Review.objects.order_by('date')
    return render(request, 'ranking/review_list.html', {'reviews': reviews})
