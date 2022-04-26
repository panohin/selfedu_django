from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from .utils import IndexMixin


urlpatterns = [
    path('', views.Main.as_view(), name='main_url'),
    path('about', views.about, name='about_url'),
    path('add_page', views.add_page, name='add_page_url'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('post/<str:slug>', views.show_post, name='post'),
    path('category/<str:slug>', views.ByCategory.as_view(), name='by_category_url')
    # path('<slug:slug>', views.post_detail, name='post_detail_url'),
]
