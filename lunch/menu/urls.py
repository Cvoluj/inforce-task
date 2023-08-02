from django.urls import path, include
from .views import MenuItemViewSet, MenuViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'items', MenuItemViewSet)
router.register(r'menus', MenuViewSet)


urlpatterns = [
    path('', include(router.urls))
]