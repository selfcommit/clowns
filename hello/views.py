from django import http
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import urllib2
import json
#https://developers.google.com/appengine/docs/python/urlfetch/
from google.appengine.api import urlfetch

bot_icon = 'https://s3-us-west-2.amazonaws.com/slack-files2/avatars/2014-08-29/2598783684_48.jpg'
#Chat message API https://api.slack.com/methods/chat.postMessage
incoming_webhook = 'https://stackexchange.slack.com/services/hooks/incoming-webhook?token=iFNL7NRbD71q0v3XgxCqq4wU'

def home(request):
    return http.HttpResponse('<head><link rel="icon" href="static/favicon.ico"></head><body><center><a href=https://www.google.com/search?q=scary+clown><img src=static/clown1.jpg></a></center></body>')

@csrf_exempt
def stackbot(request):
	if request.POST:
		token = request.POST['token']
		team_id = request.POST['team_id'].lower()
		channel_id = request.POST['channel_id'].lower()
		channel_name = request.POST['channel_name'].lower()
		user_id = request.POST['user_id'].lower()
		user_name = request.POST['user_name'].lower()
		text = request.POST['text'].lower()
		form_fields = {'text': '@'+user_name+' Please <http://g.co/hangout/stackbot'+user_name+' | Join My Meeting!>', 'username':'StackBot', 'icon_url':bot_icon, 'link_names' : '1', 'parse' : 'none', 'channel' : '#'+channel_name }
		
		data = json.dumps(form_fields)
		req = urllib2.Request(url = incoming_webhook, data = data, headers = {'content-type' : 'application/json'})
		result = urllib2.urlopen(req) 

		return http.HttpResponse('Contacting Stackbot...')
	else:
		return http.HttpResponse(request)

@csrf_exempt
def slash_stackbot(request):
	
	#if request.POST['command'].lower() == '/stackbot':
	#	command_request = request.POST['command'].lower()
	#	token = request.POST['token']
	#	team_id = request.POST['team_id'].lower()
	#	channel_id = request.POST['channel_id'].lower()
	#	channel_name = request.POST['channel_name'].lower()
	#	user_id = request.POST['user_id'].lower()
	#	user_name = request.POST['user_name'].lower()
	#	text = request.POST['text'].lower()
	#	form_fields = {'text': '@'+user_name+' Please <http://g.co/hangout/stackbot'+user_name+' | Join My Meeting!>', 'username':'StackBot', 'icon_url':bot_icon, 'link_names' : '1', 'parse' : 'none', 'channel' : '#'+channel_name }
		
	#	data = json.dumps(form_fields)
	#	req = urllib2.Request(url = incoming_webhook, data = data, headers = {'content-type' : 'application/json'})
	#	result = urllib2.urlopen(req) 

	#	return http.HttpResponse('Contacting Stackbot...')
	#else:
	return http.HttpResponse(request)
