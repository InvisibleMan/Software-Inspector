from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.models import User
from www.models import SoftLine #Soft, SoftVersion, SoftItem, SoftLine

def index(request):
	users = User.objects.all()
	return render_to_response('index.html', {
		'user':request.user,
		'users':users
	})


def login(request):
	user = request.user
	if not user.is_authenticated():
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return HttpResponseRedirect('/%s/' % username)
		
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
	
	#soft_items = SoftItem.objects.filter(user__id=user.id)
	soft_items = SoftLine.objects.filter(user=user.id).all()
	
	#return HttpResponse(user.username + '\' page!')
	return render_to_response('details.html', {
		'user':user,
		'soft_items':soft_items
	})

def post_programs(request):
	count = 0
	response = 'Welcome to API!'
	if request.method == 'POST':
		user = request.user
		if user.is_authenticated():
			#print(request.POST)
			import www.api
			count = www.api.parse_xml(request.raw_post_data, user)
		else:
			response = "Need login before"
			print("Need login before")
	else:
		print("Wrong Request Method")
	

	if(count > 0):
		response = 'Loaded %d items!' % count

	#print(response)
	return HttpResponse(response)
