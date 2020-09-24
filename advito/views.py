from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.http import HttpResponse
from .models import Add, Profile, Category
from django.template import loader


def index(request):
    '''
    вьюха для главной страницы
    '''
    post_queryset = Add.objects.order_by('-date_pub')[:7]
    context = {
        'posts': post_queryset,
    }
    return render(request, 'advito/index.html', context)


def cat_ord(request, category_id):
    '''
    вьюха для просмотра постов по категориям
    '''
    category = get_object_or_404(Category, id=category_id)
    posts = Add.objects.filter(category=category_id)
    context = {
        'posts': posts,
    }
    return render(request, 'advito/cat_ord.html', context)


def all(request):
    '''
    вьюха для страницы всех объявлений
    '''
    post_queryset = Add.objects.order_by('-date_pub')
    template = loader.get_template('advito/all.html')
    context = {
        'posts': post_queryset,
    }
    return HttpResponse(template.render(context))


def post_detail(request, add_id):
    '''
    вьюха для объявления
    '''
    try:
        post = get_object_or_404(Add, id=add_id)
    except Add.DoesNotExist:
        raise Http404("Post doesnt exist")
    context = {
        'post': post,
    }
    return render(request, 'advito/post-detail.html', context)


def category(request):
    '''
    вьюха для категорий
    '''
    categ_queryset = Category.objects.all()
    template = loader.get_template('advito/cat.html')
    context = {
        'categ': categ_queryset,
    }
    return HttpResponse(template.render(context))


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
