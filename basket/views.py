from django.shortcuts import render

# Create your views here.
def view_basket(request):
    """Renders the basket page"""

    template = 'basket/basket.html'

    return render(request, template)

