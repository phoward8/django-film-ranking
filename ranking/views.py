from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect, render
from .models import Review
from .forms import ReviewForm
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Q

def film(request, film):
    reviews = Review.objects.filter(film=film).order_by('date')
    return render(request, 'ranking/film.html', {'film': film, 'reviews': reviews})


def review_list(request):
    # TODO: Don't hardcode admin user
    return review_list2(request, User.objects.all().filter(~Q(username='User')))

def review_list2(request, users):

    if len(users) < 4:
        return render(request, 'ranking/review_list.html', {'users': users})
    else:
        # TODO: Not this
        raise Exception("UH OH!!!");

def review_new(request, film):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.date = timezone.now()
            review.score = request.score
            review.save()
            return redirect('post_detail', film=review.pk)
    
    form = ReviewForm()
    return render(request, 'ranking/review_new.html', {'form': form})
