from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('menu/', views.menu_index, name='menu-list'),
    path('menu/add/', views.menu_add, name='menu-add'),
    path('menu/update/', views.menu_update, name='menu-update'),
    path('menu/edit/<int:id>/', views.menu_edit, name='menu-edit'),
    path('menu/show/<int:id>/', views.menu_show, name='menu-show'),
    path('menu/delete/<int:id>/', views.menu_delete, name='menu-delete'),

    # category
    path('category/create/', views.category_create, name='category-create'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
