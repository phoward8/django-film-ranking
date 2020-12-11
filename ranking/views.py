from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect, render
from .models import Review
from .forms import ReviewForm
from django.utils import timezone

def film(request, film_id):
    reviews = Review.objects.filter(film=film_id).order_by('date')
    return render(request, 'ranking/film.html', {'film': film_id, 'reviews': reviews})

def review_list(request):
    User = get_user_model()
    phoebe = User.objects.filter(username='phoebe')[0]
    jon = User.objects.filter(username='jon')[0]

    reviews_phoebe = Review.objects.filter(author=phoebe).order_by('score')
    reviews_jon = Review.objects.filter(author=jon).order_by('score')

    return render(request, 'ranking/review_list.html', 
                  {'reviews_phoebe': reviews_phoebe,
                   'reviews_jon': reviews_jon})

def review_new(request, film_id):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.date = timezone.now()
            review.score = request.score
            review.save()
            return redirect('post_detail', film_id=review.pk)
    
    form = ReviewForm()
    return render(request, 'ranking/review_new.html', {'form': form})
