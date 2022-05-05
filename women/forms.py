import email
from multiprocessing import AuthenticationError
from re import A
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

from .models import Category, Women

class AddPageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Категория не выбрана"

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title



# class AddPageForm(forms.ModelForm):
# 	class Meta:
# 		model = Women
# 		fields = ['title', 'slug', 'content', 'photo', 'is_published', 'category']
# 		widgets = {'title': forms.TextInput(attrs={'class':'form-input'}),'content':forms.Textarea(attrs={'cols':68, 'rows':10})}

# 	def __init__(self, *args, **kwargs):
# 		super().__init__(*args, **kwargs)
# 		self.fields['category'].empty_label = 'Категория не выбрана'

	
# 	def clean_title(self):
# 		title = self.cleaned_data['title']
# 		if len(title) > 200:
# 			raise ValidationError('Длина заголовка слишком большая')

class RegisterUserForm(UserCreationForm):
	username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-input'}))
	email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-input'}))
	password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-input'}))
	password2 = forms.CharField(label='Пароль повторно', widget=forms.PasswordInput(attrs={'class':'form-input'}))

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')
		widgets = {
			'username': forms.TextInput(attrs={'class':'form-input'}),
			'password1': forms.PasswordInput(attrs={'class':'form-input'}),
			'password2': forms.PasswordInput(attrs={'class':'form-input'}),
		}

class UserLoginForm(AuthenticationForm):
	username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-input'}))
	password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-input'}))

class ContactForm(forms.Form):
	name = forms.CharField(label='Имя', max_length=255)
	email = forms.EmailField(label='Email')
	content = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':10}))
	captcha = CaptchaField()
	