from rest_framework.routers import DefaultRouter
from .views import DolarViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'dolar', DolarViewSet)

urlpatterns = [
    path("", include(router.urls))
]
