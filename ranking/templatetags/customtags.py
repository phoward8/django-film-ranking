from django import template
from ranking.models import Review
from django.contrib.auth.models import User

register = template.Library()

@register.simple_tag
def getReviews(user):
    return user.review.all()