from django.conf.urls import url
from advito import views
from django.urls import path


urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('all/', views.all, name='all'),
    path('category/', views.category, name='category'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<int:add_id>/', views.post_detail, name='post_detail'),
    path('post/<int:add_id>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:add_id>/delete/', views.post_delete, name='post_delete'),
    path('post/<int:add_id>/like/', views.like_post, name='like_post'),
    path('category/<int:category_id>/', views.cat_ord, name='categ'),
]