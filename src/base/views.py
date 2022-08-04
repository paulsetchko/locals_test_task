from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User, CatOrHedgehog, Lot, Bid
from .serializers import UserSerializer, CatOrHedgehogSerializer, LotSerializer, BidSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class CatOrHedgehogViewSet(viewsets.ModelViewSet):
    queryset = CatOrHedgehog.objects.all()
    serializer_class = CatOrHedgehogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(owner_id=self.request.user.id)


class LotViewSet(viewsets.ModelViewSet):
    queryset = Lot.objects.all()
    serializer_class = LotSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def choose_winner(self, request, pk, version, **kwargs):
        lot = self.get_object()
        serializer = self.serializer_class(data=request.data, instance=lot)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(self.serializer_class(instance=lot).data)

    @action(detail=True, methods=['get'])
    def bids_list(self):
        bids = Bid.objects.filter(related_lot=self.get_object())
        serializer = BidSerializer(instance=bids, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(owner_id=self.request.user.id)

