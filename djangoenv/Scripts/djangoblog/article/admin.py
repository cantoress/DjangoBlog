from django.contrib import admin
from article.models import Article, Comment


# Very strange behavior

# Register your models here.

class ArticleInline(admin.StackedInline):
    model = Comment
    extra = 2


class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title', 'article_text', 'article_date', 'article_image']
    inlines = [ArticleInline]
    list_filter = ['article_date']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
