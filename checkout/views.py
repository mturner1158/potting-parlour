from django.shortcuts import render


def checkout(request):

    template = 'checkout/checkout.html'

    return render(request, template,)


def checkout_success(request):

    template = 'checkout/checkout_success.html'

    return render(request, template,)
