from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from api.views import ApiViewSet

router = DefaultRouter()
router.register('api', ApiViewSet, basename='api')

app_name = 'api'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]