from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParkViewSet

router = DefaultRouter()
router.register(r'parks', ParkViewSet)

#юрлы
urlpatterns = [
    path('', include(router.urls))
]
