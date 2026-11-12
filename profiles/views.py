from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import UserProfileForm

from checkout.models import Order

@login_required
def view_profile(request):
    """Returns the users profile"""
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """Show the selected past order"""
    order = get_object_or_404(
        Order, order_number=order_number, user_profile__user=request.user
    )

    context = {"order": order, "from_profile": True}
    return render(request, "checkout/checkout_success.html", context)
