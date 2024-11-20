from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import YangilikViewSet, LoyihaViewSet, HodimViewSet, TaklifViewSet, TakliflarimizViewSet,\
    BoglanishViewSet


router = DefaultRouter()
router.register(r'yangilik', YangilikViewSet)
router.register(r'loyiha', LoyihaViewSet)
router.register(r'hodim', HodimViewSet)
router.register(r'taklif', TaklifViewSet)
router.register(r'takliflarimiz', TakliflarimizViewSet)
router.register(r'boglanish', BoglanishViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
