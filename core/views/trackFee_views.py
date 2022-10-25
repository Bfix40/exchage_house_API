from rest_framework.viewsets import ModelViewSet
from ..serializers import TrackFeeSerializer
from ..models import TrackFee


class TrackFeeViewSet(ModelViewSet):

    serializer_class = TrackFeeSerializer

    def get_queryset(self):
        return TrackFee.objects.all()
