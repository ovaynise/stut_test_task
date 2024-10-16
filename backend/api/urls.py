from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApiViewSet

router = DefaultRouter()
router.register(r'api', ApiViewSet, basename='api')

urlpatterns = [
    path('', include(router.urls)),
]