from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def index(request):
    is_logged = False
   
    message = 'Hello, Anonymous!'

    if(request.method == 'POST' and len(request.POST['email']) > 0):
        email = request.POST['email']
        
        is_logged = True
        #user = authenticate(username='Homer', password='1')
        user = User.objects.get(username__exact='Homer')
        if user is not None:
            user = authenticate(username='Homer', password='1')
            login(request, user)
            message = 'Hello, ' +  user.username
        else:
            message = 'Hello, ' +  email
        
        
        
    return render_to_response('index.html', {
        'is_logged':is_logged, 'message':message
        })
#    return HttpResponse('Ok')

#    fullevents = [loader.render_to_string('event2.html', { 'event': one_math }) for one_math in mathes]
#    return render_to_response('index.html', {'events': fullevents})

#def authenticate(self, username=None):