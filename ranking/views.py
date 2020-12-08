from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from .models import Film, Review

def film(request, pk):
    film = get_object_or_404(Film, pk=pk)
    return render(request, 'ranking/film.html', {'film': film})

def review_list(request):
    User = get_user_model()
    phoebe = User.objects.filter(username='phoebe')[0]
    jon = User.objects.filter(username='jon')[0]

    reviews_phoebe = Review.objects.filter(author=phoebe).order_by('score')
    reviews_jon = Review.objects.filter(author=jon).order_by('score')

    return render(request, 'ranking/review_list.html', 
                  {'reviews_phoebe': reviews_phoebe,
                   'reviews_jon': reviews_jon})
