from django.urls import path
from .views import park_list, park_detail # Импортируем обе view

app_name = 'frontend'

urlpatterns = [
    # 1. URL для списка всех парков (главная страница)
    path('', park_list, name='park-list'),
    
    # 2. URL для детальной страницы ОДНОГО парка
    path('parks/<int:park_id>/', park_detail, name='park-detail'),
]