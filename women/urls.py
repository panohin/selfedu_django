from django.contrib import admin
from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('', views.main, name='main_url'),
    path('about', views.about, name='about_url'),
    path('add_page', views.add_page, name='add_page'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('post/<int:post_id>', views.show_post, name='post'),
    path('category/<int:cat_id>', views.by_category, name='by_category_url')
    # path('<slug:slug>', views.post_detail, name='post_detail_url'),
]
