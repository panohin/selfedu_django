from django.shortcuts import render
from django.core.cache import cache
from django.db.models import Count

from women.models import Category

class IndexMixin:
    title = None
    posts = None
    categories = None
    category_selected = None
    menu = None
    context = None
    def get(self, request):
    	if len(posts) < 1:
        	return page_not_found(request)
    	else:
        	return render(request, 'women/index.html', context=self.context)

class DataMixin:
    paginate_by = 5

    def get_user_context(self, **kwargs):
        context = kwargs
        categories = cache.get('categories')
        if not categories:
            categories = Category.objects.annotate(Count('women'))
            cache.set('categories', categories, 60)
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context