from django import forms
from django.core.exceptions import ValidationError

from .models import Category, Women

class AddPageForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['category'].empty_label = 'Категория не выбрана'

	class Meta:
		model = Women
		fields = ['title', 'slug', 'content', 'photo', 'is_published', 'category']
		widgets = {'title': forms.TextInput(attrs={'class':'form-input'}),
		'content':forms.Textarea(attrs={'cols':68, 'rows':10})}

	def clean_title(self):
		title = self.cleaned_data['title']
		if len(title) > 200:
			raise ValidationError('Длина заголовка слишком большая')