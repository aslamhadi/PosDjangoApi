from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def home_view(request):
    context = {
        'user': request.user,
    }
    return render_to_response("index.html", context)

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
