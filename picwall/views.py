# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
import time
from datetime import date
from picwall.models import pw_pic, pic_comment
from myForms import Login_Form
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def index(request):
    return HttpResponse('Hello Picwall!')


def log_in(request):
    if request.user.is_authenticated():
	return HttpResponseRedirect('/picwall/home/')
    login_prompt = ''
    if request.method == 'POST':
#	form = Login_Form(request.POST)
#	if form.is_valid():
#	    username = form.cleaned_data['name']
#	    password = form.cleaned_data['pwd']
	email = request.POST['email']
	password = request.POST['password']
#	user = authenticate(username = username, password = password)
	users = User.objects.filter(email = email)
	if len(users) > 0:
	    user = authenticate(username = users[0].username, password = password)
	    if user is not None:
		if user.is_active:
		    login(request, user)
		    return HttpResponseRedirect('/picwall/home/')
		    #redirect to a success page
		else:
		    login_promt = 'Invalid user'
	    	    #return a 'disable account' error message
	    else:
		login_prompt = 'Password is wrong'
		#return invalid login!
	else:
	    login_prompt = 'E-mail is invalid'
	    #return HttpResponse('invalid login!')
#   else:
#	form = Login_Form()

    return render(request, 'picwall/login.html',{'login_prompt':login_prompt,})

def log_out(request):
   logout(request)
   return HttpResponseRedirect('/picwall/login/')

def register(request):
    if request.user.is_authenticated():
	return HttpResponseRedirect('/picwall/home/')

    register_prompt = ''
    if request.method == 'POST':
	name = request.POST['name']
	email = request.POST['email']
	pwd = request.POST['password']
	users1 = User.objects.filter(email = email)
	users2 = User.objects.filter(username = name)
	if len(users1) == 0:
	    if len(users2) == 0:
		user = User.objects.create_user(name, email, pwd)
		user.save()
		register_prompt = 'Succeed to register! Now Please log in!'
		user = authenticate(username = name, password = pwd)
		login(request, user)
		return HttpResponseRedirect('/picwall/home/')
	    else:
		register_prompt = 'The name have been registered!'
	else:
	    register_prompt = 'Your email have been registered!'
    return render(request, 'picwall/register.html', {'register_prompt':register_prompt,})
    
def upload_pic(request):
    if request.method == 'POST':
	pic = pw_pic()
	pic_data = request.FILES['pic']
	pic.pic_name = request.POST['title']
	pic.pic_desc = request.POST['desc']
	pic.pic_upload_time = timezone.now()
	pic.pic_id = '%s_%s_%s'%(str(request.user), str(time.asctime(time.localtime())).replace(':', '_').replace(' ', '_'), pic.pic_name)
	pic.pic_url = '/tmp/'+pic.pic_id
	pic.pic_author = request.user
	pic.save()
#	pic_url ='/home/jeremy/JJ/files/images/' + pic.pic_id
	pic_url = os.path.join(BASE_DIR, 'files/images/' + pic.pic_id)
	des_origin_f = open(pic_url, "ab")
	for chunk in pic_data.chunks():  
	    des_origin_f.write(chunk)  
	des_origin_f.close()   

	return HttpResponseRedirect('/picwall/home/')


def find_pic(request, pic_id):
	image_data = open('/home/jeremy/JJ/files/images/'+pic_id, "rb").read()
	return HttpResponse(image_data, mimetype="image/jpeg")


def index_pic(request):
    if not request.user.is_authenticated():
	return HttpResponseRedirect('/picwall/login')
    pics = request.user.pw_pic_set.all()
    return render(request, 'picwall/index.html', {'pics': pics, 'username': str(request.user),})

def index_picWall(request):
    if not request.user.is_authenticated():
	return HttpResponseRedirect('/picwall/login/')
    pics = request.user.pw_pic_set.all()
    return render(request, 'picwall/index.html', {'pics': pics, 'username': str(request.user),})



def pic_info(request, pic_id):
    if not request.user.is_authenticated():
	return HttpResponseRedirect('/picwall/home')
    pic = get_object_or_404(pw_pic, pic_id = pic_id)
    comments = pic.pic_comment_set.all()
    return render(request, 'picwall/comment.html', {'pic_info':pic,'comments':comments,})

def publish_comment(request):
    if request.method == 'POST':
	comment = pic_comment()
	comment.content = request.POST['content']
	comment.author = request.user
	pic = get_object_or_404(pw_pic, pic_id = request.POST['pic_id'])
	comment.pic = pic
	comment.published_date = date.today() 	
	comment.save()
	return HttpResponseRedirect('/picwall/pic_info/'+pic.pic_id)





