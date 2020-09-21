from django.shortcuts import render
from django.http import HttpResponse
from .models import Add, Profile, Category
from django.template import loader

def index(request):
    '''
    вьюха для главной страницы
    '''
    post_queryset = Add.objects.filter('-date_pub')[:7]
    template = loader.get_template('advito/index.html')
    context = {
        'posts': post_queryset,
    }
    return HttpResponse(template.render(context))


def all(request):
    '''
    вьюха для страницы новых объявлений
    '''
    responce = "Всем привет! Добро пожаловать на доску объявлений - advito!"
    return HttpResponse(responce)


def post_detail(request, add_id):
    '''
    вьюха для объявления
    '''
    post = Add.objects.get(id=add_id)
    responce = "Автор:{}| Название:{}| Описание:{}".format(post.author, post.header, post.description)
    return HttpResponse(responce)


def category(request, category_id):
    '''
    вьюха для объявлений по категориям
    '''
    post = Add.objects.get(id=add_id)
    responce = "Автор:{}| Название:{}| Описание:{}".format(post.author, post.header, post.description)
    return HttpResponse(responce)


def post_edit(request, add_id):
    '''
    вьюха для редактирования объявления
    '''
    post = Add.objects.get(id=add_id)
    responce = "Редактирование поста Автор:{}| Название:{}| Описание:{}".format(post.author, post.header, post.description)
    return HttpResponse(responce)


def post_create(request):
    '''
    вьюха для создания объявления
    '''
    responce = "Создание объявления"
    return HttpResponse(responce)


def post_delete(request, add_id):
    '''
    вьюха для удаления объявления
    '''
    post = Add.objects.get(id=add_id)
    responce = "Удаление поста Автор:{}| Название:{}| Описание:{}".format(post.author, post.header, post.description)
    return HttpResponse(responce)


def like_post(request, add_id):
    '''
    вьюха для добавления объявления в избранное
    '''
    post = Add.objects.get(id=add_id)
    responce = "Добавить в избранное пост Автор:{}| Название:{}| Описание:{}".format(post.author, post.header, post.description)
    return HttpResponse(responce)
