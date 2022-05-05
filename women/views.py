from multiprocessing import AuthenticationError
from re import template
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import View, ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.views import LoginView

from .utils import IndexMixin, DataMixin
from .models import Women, Category
from .forms import AddPageForm, RegisterUserForm, UserLoginForm, ContactForm

def page_not_found(request):
    return HttpResponse("4 0 4 Страница не найдена")

def about(request):
    title = 'О сайте'
    return render(request, 'women/about.html', {'title':title})

def paginator(request):
    title = 'Пример испрользования пагинатора в функции-представлении'
    contact_list = Women.objects.all()
    paginator = Paginator(contact_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'women/about.html', {'title':title, 'page_obj':page_obj})

def contact(request):
    return HttpResponse('Contact info')

def logout_user(request):
    logout(request)
    return redirect('main_url')

class Main(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return context | c_def

    def get_queryset(self):
        return Women.objects.filter(is_published=True).select_related('category')

class ByCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.get(slug=self.kwargs['slug'])
        c_def = self.get_user_context(title='Категория - ' + str(category.name), cat_selected=category.pk)
        return context | c_def
  
    def get_queryset(self):
        return Women.objects.filter(category__slug=self.kwargs['slug'], is_published=True).select_related('category')

class ShowPost(DetailView):
    model = Women
    template_name = 'women/post_detail.html'
    context_object_name = 'post'

class AddPage(LoginRequiredMixin, CreateView):
    form_class = AddPageForm
    template_name = 'women/add_page.html'
    success_url = reverse_lazy('main_url')
    login_url = reverse_lazy('main_url')
    
class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'women/register.html'
    success_url = reverse_lazy('main_url')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return context | c_def

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main_url')

class LoginUser(DataMixin, LoginView):
    # form_class = UserLoginForm
    form_class = UserLoginForm
    template_name = 'women/login.html'
    
    def get_success_url(self):
        return reverse_lazy('main_url')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return context | c_def

class ContactView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'women/contact.html'
    success_url = reverse_lazy('main_url')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Обратная связь')
        return context | c_def
    def form_valid(self, form):
        return redirect('main_url')
