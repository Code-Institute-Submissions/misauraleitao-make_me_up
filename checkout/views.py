from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag honey !")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KMEw5L776LISPZfWiAVgBBi8mRzyGbXVP84QUlpPUC1Y1dcH4nPPiWbEpNB7O36Q8hR1YISRCHLW1Hlg8C4ThMg00TRLKxuks',
        'client_secret_key' : 'test client server'
    }

    return render(request, template, context)
