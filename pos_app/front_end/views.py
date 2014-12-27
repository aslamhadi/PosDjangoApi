from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required


@login_required
def home_view(request):
    context = {
        'user': request.user,
    }
    return render_to_response("index.html", context)
