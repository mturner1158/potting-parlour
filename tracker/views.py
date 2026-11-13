from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def view_tracker(request):
    """Shows tracker for plants the user has bought"""

    template = "tracker/tracker.html"

    return render(request, template,)

