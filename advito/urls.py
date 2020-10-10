from django.conf.urls import url
from advito import views
from django.urls import path
from django.views.generic import TemplateView
from advito.views import SignupView, LoginView, EditProfileView, ProfileView, logout_view
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    path('all/', views.AllView.as_view(), name='all'),
    path('category/', views.category, name='category'),
    path('post/create/', views.CreatePostView.as_view(), name='post_create'),
    path('post/<int:add_id>/', views.PostView.as_view(), name='post_detail'),
    # path('post/<int:add_id>/edit/', views.EditPostView.as_view(), name='post_edit'),
    # path('post/<int:add_id>/delete/', views.DeletePostView.as_view(), name='post_delete'),
    path('category/<int:category_id>/', views.cat_ord, name='categ'),
    path('category/create/', views.categ_create, name='categ_create'),
    # path('post/<int:add_id>/delete_success/', TemplateView.as_view(template_name='advito/delete_success.html'), name='delete-post-success'),
    # path('login/', views.LoginView.as_view(), name='login'),
]


urlpatterns += [
    path('login/', LoginView.as_view(), name='login'),
    # path('logout/', logout_view, name='logout'),
    path('<int:user_id>/profile/', ProfileView.as_view(), name='profile'),
    path('<int:user_id>/profile/edit', login_required(EditProfileView.as_view()), name='edit-profile'),
    path('signup/', SignupView.as_view(), name='signup'),
]