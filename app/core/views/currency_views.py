from rest_framework.viewsets import ModelViewSet
from ..serializers import CurrencySerializer
from ..models import Currency


class CurrencyViewSet(ModelViewSet):

    serializer_class = CurrencySerializer

    def get_queryset(self):
        return Currency.objects.all()
