from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate


def home_view(request):
    return render_to_response("index.html")
    # if request.user.is_authenticated():
    #     if request.user.is_superuser:
    #         return HttpResponseRedirect(reverse('account:index'))
    # return HttpResponseRedirect(reverse('account:login'))

def login_view(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            return HttpResponseRedirect(reverse('home'))
            # if user.is_active and user.is_superuser:
            #     login(request, user)
            #     return HttpResponseRedirect(reverse('account:index'))
            # else:
            #     return HttpResponse("Your account has not been activated.")
        else:
            # print "Invalid login details: {0}, {1}".format(email, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('account/login.html', {}, context)
