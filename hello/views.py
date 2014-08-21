from django import http

def home(request):
    return http.HttpResponse('<center><a href=https://www.google.com/search?q=scary+clown><img src=static/clown1.jpg></a></center>')
