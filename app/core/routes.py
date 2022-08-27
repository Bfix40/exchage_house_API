

from rest_framework.routers import DefaultRouter

from .views.currency_views import CurrencyViewSet
from .views.trackFee_views import TrackFeeViewSet

from .views.users_views import UserViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='users')
router.register(r'currency', CurrencyViewSet, basename='currency')
router.register(r'trackfee', TrackFeeViewSet, basename='trackfee')

