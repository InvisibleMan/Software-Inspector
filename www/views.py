from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import Http404

def index(request):
    return render_to_response('index.html', {
        'user':request.user
    })


def login(request):
    user = request.user
    if not user.is_authenticated():
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
        
    return render_to_response('index.html', {
        'user':user
    })

def logout(request):
    auth.logout(request)
    return index(request)

def user(request, user_name):
    user = None
    try:
        user = User.objects.get(username__iexact=user_name)
        user.username
    except User.DoesNotExist:
        raise Http404#render_to_response('404.html')
        
    return HttpResponse(user.username + '\' page!')

        #try:
        #    user = User.objects.get(email__exact='fairness@mail.ru')
        #except:
        #    pass