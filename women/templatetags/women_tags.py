from django import template

from women.models import *

register = template.Library()

@register.simple_tag()
def get_all_categories():
	return Category.objects.all()

@register.inclusion_tag('women/list_categories.html')
def show_cats():
	cats = Category.objects.all()
	result = {'cats': cats} 
	return result