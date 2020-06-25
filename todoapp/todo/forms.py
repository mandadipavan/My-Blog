from django import forms
from django.forms import ModelForm
from .models import ModelData

class TodoForm(forms.ModelForm):

	class Meta:
		model = ModelData
		fields = ['title']