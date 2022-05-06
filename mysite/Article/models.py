from django.db import models
from django.urls import reverse  # Или reverse_lazy


# Модель статьи.
class Article(models.Model):
    title = models.CharField(max_length=90, verbose_name='Наименование')
    content = models.TextField(verbose_name='Описание')
    examples = models.TextField(verbose_name='Примеры', blank=True)
    solution = models.TextField(verbose_name='Решение', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано?')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    views = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        ordering = ['created_at']  # Сортировка по дате создания

    def get_absolute_url(self):
        return reverse('article', kwargs={'article_id': self.pk})

    def __str__(self):
        return self.title


# Модель категорий
class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']  # Сортировка по title

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title
