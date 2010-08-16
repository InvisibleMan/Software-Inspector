from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import Http404
from www.models import Soft, SoftVersion, SoftItem


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
    
    soft_items = SoftItem.objects.filter(user__id=user.id)
    
    #return HttpResponse(user.username + '\' page!')
    return render_to_response('details.html', {
        'user':user,
        'soft_items':soft_items
    })

def post_programs(request):
    if request.method == 'POST':
        print(request.POST)
    else:
        print("Wrong Request Method")
        
    return HttpResponse('Welcome to API!')

        