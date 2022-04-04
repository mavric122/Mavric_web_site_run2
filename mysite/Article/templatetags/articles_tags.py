from django import template

from ..models import Category

register = template.Library()


# Получение всех категорий
@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()
