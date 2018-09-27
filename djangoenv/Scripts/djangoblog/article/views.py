from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
from django.template.loader import get_template
from article.models import Article, Comment
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


def articles(request):
    return render_to_response('articles.html', {'articles': Article.objects.all()})


def article(request, article_id=1):
    return render_to_response('article.html', {'article': Article.objects.get(id=article_id), 'comments': Comment.objects.filter(comments_article_id=article_id)})
