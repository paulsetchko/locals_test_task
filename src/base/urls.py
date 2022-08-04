from django.urls import path, include
from rest_framework import routers

from base.views import BidViewSet, LotViewSet, CatOrHedgehogViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'animals', CatOrHedgehogViewSet)
router.register(r'lots', LotViewSet)
router.register(r'bids', BidViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

