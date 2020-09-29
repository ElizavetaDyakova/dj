from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.http import HttpResponse
from django.db.models import Sum
from .models import Add, Profile, Category
from django.template import loader
from .forms import PostForm, CatForm


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
    posts = Add.objects.filter(category=category)
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
    form = PostForm()
    template_name = 'advito/post_create.html'
    context = {'form': form}
    if request.method == "GET":
        return render(request, template_name, context)
    elif request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            context['post_was_created'] = True
            return render(request, template_name, context)
        else:
            context['post_was_created'] = False
            context['form'] = form
            return render(request, template_name, context)

    return render(request, 'advito/post_create.html', {'form': form})


def post_delete(request, add_id):
    '''
    вьюха для удаления объявления
    '''
    post = Add.objects.get(id=add_id)
    responce = "Удаление поста Автор:{}| Название:{}| Описание:{}".format(post.author, post.header, post.description)
    return HttpResponse(responce)


def categ_create(request):
    '''
    вьюха для создания объявления
    '''
    form_cat = CatForm()
    template_name = 'advito/cat_create.html'
    context = {'form': form_cat}
    if request.method == "GET":
        return render(request, template_name, context)
    elif request.method == "POST":
        form_cat = PostForm(request.POST)

        if form_cat.is_valid():
            cat = form_cat.save(commit=False)
            cat.author = request.user
            cat.save()
            context['cat_was_created'] = True
            return render(request, template_name, context)
        else:
            context['cat_was_created'] = False
            context['form_cat'] = form_cat
            return render(request, template_name, context)

    return render(request, 'advito/cat_create.html', {'form_cat': form_cat})


def like_post(request, add_id):
    '''
    вьюха для добавления объявления в избранное
    '''
    post = Add.objects.get(id=add_id)
    if request.user in post.favourites.all():
        like = post.favourites.get(pk=request.user.id)
        post.favourites.remove(like)
    else:
        post.favourites.add(request.user)
        post.save()
    return redirect(request.META.get('HTTP_REFERER'), request)
