from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('mail_send', views.mail_send, name='mail_send'),
]

