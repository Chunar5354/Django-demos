from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages



def index(request):
	return render(request, 'index.html')

def mail_send(request):
	send_mail(
		'Chunar sends you a message.',
		'hellow man',
		'123456@qq.com',
		['654321@qq.com',],
		fail_silently = False,
	)
	messages.success(request, 'Successfully sended')
	return HttpResponseRedirect('/')
# Create your views here.
