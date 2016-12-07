from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

from pos_app.account.models import User


def login_view(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse("Username atau password ada yang salah.")
    else:
        return render_to_response('account/login.html', {}, context)


def register_view(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        new_user = authenticate(username=username, password=password)
        login(request, new_user)
        return HttpResponseRedirect(reverse('home'))
    else:
        return render_to_response('account/register.html', {}, context)
