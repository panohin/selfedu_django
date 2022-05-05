from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from .utils import IndexMixin
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', views.Main.as_view(), name='main_url'),
    path('about', views.about, name='about_url'),
    path('add_page', views.AddPage.as_view(), name='add_page_url'),
    path('contact', views.ContactView.as_view(), name='contact_url'),
    path('logout', views.logout_user, name='logout_url'),
    path('login', views.LoginUser.as_view(), name='login_url'),
    path('register', views.RegisterUser.as_view(), name='register_url'),
    path('post/<str:slug>', views.ShowPost.as_view(), name='post'),
    path('category/<str:slug>', views.ByCategory.as_view(), name='by_category_url'),
    path('paginator', views.paginator, name='paginator_url'),
    path('__debug__/', include('debug_toolbar.urls')),
]
