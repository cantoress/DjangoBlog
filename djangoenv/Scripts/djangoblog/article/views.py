from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, render_to_response, redirect
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from article.models import Article, Comment
from article.forms import CommentForm
from django.views.decorators.csrf import csrf_protect
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


@csrf_protect
def article(request, article_id=1):
    comment_form = CommentForm
    args = {}
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comment.objects.filter(comments_article_id=article_id)
    args['form'] = comment_form
    return render(request, 'article.html', args)


def addlike(request, article_id):
    try:
        if article_id in request.COOKIES:
            redirect('/')
        else:
            article_for_likes = Article.objects.get(id=article_id)
            article_for_likes.article_likes += 1
            article_for_likes.save()
            response = redirect('/')
            response.set_cookie(article_id, 'test')
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')


@csrf_protect
def addcomment(request, article_id):
    if request.POST and ("pause" not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/articles/get/%s' % article_id)


