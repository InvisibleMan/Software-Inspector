from django.http import HttpResponse
#from mysite.polls.models import Poll

def index(request):
    return HttpResponse('Ok')