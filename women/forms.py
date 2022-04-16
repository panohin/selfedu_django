from django import forms

class AddPageForm(forms.Form):
	post_title = forms.CharField(max_length=25)
	post_content = forms.CharField(max_length=200)