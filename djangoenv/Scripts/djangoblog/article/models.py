from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Article(models.Model):
    class Meta:
        db_table = "article"

    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_date = models.DateTimeField()
    article_likes = models.IntegerField(default=0)
    article_image = models.ImageField(upload_to='images/', blank=True, null=True)


class Comment(models.Model):
    class Meta:
        db_table = 'comments'

    comments_text = models.TextField(verbose_name="Your comment")
    comments_article = models.ForeignKey(Article, on_delete='PROTECT')
    comments_author = models.ForeignKey(User, on_delete='PROTECT', default=1)
    comments_date = models.DateTimeField()
