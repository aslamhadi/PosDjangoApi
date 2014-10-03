from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response


def home_view(request):
    return render_to_response("index.html")
    # if request.user.is_authenticated():
    #     if request.user.is_superuser:
    #         return HttpResponseRedirect(reverse('account:index'))
    # return HttpResponseRedirect(reverse('account:login'))