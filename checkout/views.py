from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, reverse

from .forms import OrderForm

def checkout(request):
    basket = request.session.get('basket', {})

    if not basket:
        messages.error(request, "There is nothing in your basket")
        return redirect(reverse('all_plants'))

    order_form = OrderForm()

    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
    }

    return render(request, template, context)


def checkout_success(request):

    template = 'checkout/checkout_success.html'

    return render(request, template,)
