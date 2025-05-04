from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponsePermanentRedirect,  HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify, cut


# Create your views here.

menu = [{'title':'О сайте', 'url_name':'about'},
    {'title':'Добавить статью', 'url_name':'add_page'},
    {'title':'Обратная связь', 'url_name':'contact'},
    {'title':'Войти', 'url_name':'login'},
    {'title':'Тестовая кнопка', 'url_name':'my_test'}]

data_db = [
    {"id": 1, "name": "Item 1", "content": "Content for item 1", "is_public": True},
    {"id": 2, "name": "Item 2", "content": "Content for item 2", "is_public": False},
    {"id": 3, "name": "Item 3", "content": "Content for item 3", "is_public": True},
    {"id": 4, "name": "Item 4", "content": "Content for item 4", "is_public": False},
    {"id": 5, "name": "Item 5", "content": "Content for item 5", "is_public": True},
    {"id": 6, "name": "Item 6", "content": "Content for item 6", "is_public": False},
    {"id": 7, "name": "Item 7", "content": "Content for item 7", "is_public": True},
    {"id": 8, "name": "Item 8", "content": "Content for item 8", "is_public": False},
    {"id": 9, "name": "Item 9", "content": "Content for item 9", "is_public": True},
    {"id": 10, "name": "Item 10", "content": "Content for item 10", "is_public": False},
]



def index(request):
    #t = render_to_string('women/index.html')
    #return HttpResponse(t)
    data = {'title':'шаблон index ',
            'menu': menu,
            'posts': data_db}
    return render(request, 'women/index.html', context=data)

def about(request):
    data = {'title': 'шаблон about'}
    return render(request, 'women/about.html', data)

def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id {post_id}')

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

def addpage(request):
    return HttpResponse('Добавление статьи')

def contact(request):
    return HttpResponse('Обратная связь') 

def login(request):
    return HttpResponse('Авторизация')

def test(request):
    return HttpResponse('Тест')

