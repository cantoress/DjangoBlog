from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
# Create your views here.


def basic(request):
    view = "basic"
    html = "<html><head></head><body><h1>This is %s view</h1></body></html>" % view
    return HttpResponse(html)


def template(request):
    view = "templatefff"
    t = get_template('basic_view.html')
    html = t.render({'name': view})
    return HttpResponse(html)


def useful(request):
    view = "useful"
    return render_to_response('basic_view.html', {'name': view})