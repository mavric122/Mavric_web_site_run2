from django import forms
from .models import Category  # Для выбора категорий из списка


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=150, label='Тема',
                            widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'rows': 5
                            }))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={
                                'class': 'form-control',
                                'rows': 10
                            }))
    examples = forms.CharField(label='Примеры', widget=forms.Textarea(attrs={
                                'class': 'form-control',
                                'rows': 10
                            }))
    solution = forms.CharField(label='Решение', widget=forms.Textarea(attrs={
                                'class': 'form-control',
                                'rows': 10
                            }))
    is_published = forms.BooleanField(label='Опубликовано?')
    category = forms.ModelChoiceField(empty_label='Выберите категорию',label='Категория',
                                      queryset=Category.objects.all(), widget=forms.Select(attrs={
                                'class': 'form-control'
                            }))  # Для выбора категорий из списка