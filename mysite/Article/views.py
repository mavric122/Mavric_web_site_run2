from django.shortcuts import render, get_object_or_404, redirect

from .models import Article, Category
from .forms import ArticleForm


# Функция главной страницы
# Функция всех категорий вынесена в articles_tags
def title_menu(request):
    article = Article.objects.all()
    context = {'article': article,
               'title': 'Список статей',
               }
    return render(request, 'mysite/title.html', context)


# Функция страницы категории
# Функция всех категорий вынесена в articles_tags
def get_category(request, category_id):
    article = Article.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {'article': article,
               'title': 'Список статей',
               'category': category,  # Категории по id
               }
    return render(request, 'mysite/category.html', context)


# Страница с выбранной категорией
def view_article(request, article_id):
    # article_item = Article.objects.get(pk=article_id)
    article_item = get_object_or_404(Article, pk=article_id)
    content = {'article_item': article_item
               }
    return render(request, 'mysite/view_article.html', content)


# Добавить статью
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = Article.objects.create(**form.cleaned_data)
            return redirect(article)
    else:
        form = ArticleForm()
    return render(request, 'mysite/add_article.html', {'form': form})
