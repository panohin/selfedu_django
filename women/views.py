from django.shortcuts import render
from django.http import HttpResponse

from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about_url'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
]

def page_not_found(request):
    return HttpResponse("4 0 4 Страница не найдена")


def main(request):
    title = 'Главная страница'
    posts = Women.objects.all()
    categories = Category.objects.all()
    category_selected = 0
    context = {'title':title,
                'menu':menu,
                'posts':posts,
                'categories':categories,
                'category_selected':category_selected
    }
    return render(request, 'women/index.html', context=context)

def about(request):
    title = 'О сайте'
    return render(request, 'women/about.html', {'title':title, 'menu':menu})

def post_detail(request, slug):
    woman_content = Women.objects.filter()
    return render(request, 'women/post_detail.html')

def by_category(request, cat_id):
    categories = Category.objects.all()
    posts = Women.objects.filter(category=cat_id)
    category_selected = cat_id
    if len(posts) < 1:
        return page_not_found(request)
    else:
        return render(request, 'women/index.html', context={"posts":posts, "category_selected":category_selected,
        "categories":categories})

def add_page(request):
    return HttpResponse('Add new page')

def contact(request):
    return HttpResponse('Contact info')

def login(request):
    return HttpResponse('Log in page')

def show_post(request, post_id):
    woman = Women.objects.get(pk=post_id)
    context = {'woman':woman}
    return render(request, 'women/about.html', context=context)

