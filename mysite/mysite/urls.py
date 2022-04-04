from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Article.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', title_menu, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('article/<int:article_id>/', view_article, name='article'),
    path('article/add-article/', add_article, name='add_article'),
]

# Загрузка медиа(фото)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
