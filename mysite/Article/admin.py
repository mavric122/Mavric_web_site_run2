from django.contrib import admin

from .models import Article, Category


# Модель записей в админке
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_ad', 'updated_ad', 'is_published')


# Модель категорий в админке
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Article)
admin.site.register(Category)
