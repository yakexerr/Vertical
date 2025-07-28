from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParkViewSet, EntertainmentViewSet

router = DefaultRouter()
router.register(r'parks', ParkViewSet)
router.register(r'entertainments', EntertainmentViewSet)

#юрлы
urlpatterns = [
    path('', include(router.urls))
]
