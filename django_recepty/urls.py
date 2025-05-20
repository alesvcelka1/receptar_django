from django.contrib import admin
from django.urls import path
from library import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('recepty/', views.recepty_list, name='recepty_list'),
    path('kuchari/', views.kuchari_list, name='kuchari_list'),
    path('kategorie/', views.kategorie_list, name='kategorie_list'),
    path('recepty/<int:pk>/', views.recept_detail, name='recept_detail'),
    path('kategorie/<int:pk>/', views.kategorie_detail, name='kategorie_detail'),
    path('kuchari/<int:pk>/', views.kuchar_detail, name='kuchar_detail'),
    path('recepty/pridat/', views.recept_create, name='recept_create'),
    path('recepty/<int:pk>/upravit/', views.recept_update, name='recept_update'),
    path('recepty/<int:pk>/smazat/', views.recept_delete, name='recept_delete'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
