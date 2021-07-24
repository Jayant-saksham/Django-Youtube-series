from django.shortcuts import redirect, render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .form import CreateArticle

# Create your views here.

def article(request):
    articles = Article.objects.all()
    data = {
        'articles': articles
    }
    return render(request, 'article.html', data)


def comment(request):
    return render(request, 'comment.html')


def article_details(request, slug):
    articles = Article.objects.get(slug = slug)
    data = {
        'articles': articles
    }
    return render(request, 'article_details.html', data)

@login_required(login_url="login_view")
def create_article(request):
    if request.method == 'POST':
        data = CreateArticle(request.POST, request.FILES)
        if data.is_valid():
            instance = data.save(commit = False)
            instance.user = request.user
            instance.save()
            return redirect("article_list")

    form = CreateArticle()
    return render(request, 'create_articles.html', {'form': form})