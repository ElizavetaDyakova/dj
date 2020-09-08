from django.conf.urls import url
from advito import views
from django.urls import path


urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    path('num', views.num),
]