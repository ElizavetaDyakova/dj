from django.shortcuts import render
from django.http import HttpResponse
from .models import Add, Profile, Category

def index(request):
    '''
    вьюха для главной страницы
    '''
    return HttpResponse('Доска объявлений')


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
    responce = "Детальное представление объявления №{}".format(add_id)
    return HttpResponse(responce)


def category(request, category_id):
    '''
    вьюха для объявлений по категориям
    '''
    responce = "Категория №{}".format(category_id)
    return HttpResponse(responce)


def post_edit(request, add_id):
    '''
    вьюха для редактирования объявления
    '''
    responce = "Редактирование объявления №{}".format(add_id)
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
    responce = "Удаление объявления №{}".format(add_id)
    return HttpResponse(responce)


def like_post(request, add_id):
    '''
    вьюха для добавления объявления в избранное
    '''
    responce = "Добавить в избранное объявление №{}".format(add_id)
    return HttpResponse(responce)
