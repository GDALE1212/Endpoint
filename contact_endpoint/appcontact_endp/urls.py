from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet

# Register ViewSet with a router
router = DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contacts')

urlpatterns = [
    path('', include(router.urls)),
]
