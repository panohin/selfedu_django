from django.shortcuts import render

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
