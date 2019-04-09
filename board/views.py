from django.shortcuts import render, redirect
from .models import Article


# Create your views here.
def article_new(request):
    return render(request, 'board/new.html')


def article_create(request):
    article = Article()
    article.title = request.POST.get('input_title')
    article.content = request.POST.get('input_content')
    article.save()
    return redirect(f'/board_ad/articles/{article.id}')


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'board/list.html', {
        'articles': articles,
    })


def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'board/detail.html', {
        'article': article,
    })


def article_edit(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'board/edit.html', {
        'article': article,
    })


def article_update(request, article_id):
    article = Article.objects.get(id=article_id)
    article.title = request.POST.get('input_title')
    article.content = request.POST.get('input_content')
    article.save()
    return redirect(f'/board_ad/articles/{article.id}')


def article_delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('/board_ad/articles')


def index(request):
    return render(request, 'board/index.html')


def greeting(request, name, role):  # Context 를 넘겨받음
    if name == 'admin':
        return render(request, 'board/greeting.html', {
            'name': 'Master_user',
            'role': 'Master',
        })

    return render(request, 'board/greeting.html', {
        'name': name.upper(),
        'role': role,
    })
