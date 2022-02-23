from django.shortcuts import render, get_object_or_404
from .models import Reviews

# Create your views here.

def reviews(request):
    """ A view to show all posts """

    reviews = Reviews.objects.all()

    context = {
        'reviews': review,
    }

    return render(request, 'reviews/reviews.html', context)

