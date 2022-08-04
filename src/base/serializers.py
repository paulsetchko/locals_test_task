from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from base.models import User, CatOrHedgehog, Bid, Lot


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "account_balance"]


class CatOrHedgehogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CatOrHedgehog
        fields = "__all__"


class BidSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bid
        fields = "__all__"

    def validate(self, attrs):
        lot = attrs.get('related_lot')
        if lot.awarded_bid is not None:
            raise ValidationError(f'You cannot submit a bid for a closed auction')
        if attrs.get('amount') < lot.price:
            raise ValidationError(f'Minimal Bid amount is {lot.price}')

        return super().validate(attrs)


class LotSerializer(serializers.HyperlinkedModelSerializer):
    bids = BidSerializer(source='bid_set', many=True, read_only=True)

    class Meta:
        model = Lot
        fields = "__all__"

    def validate(self, attrs):
        animal = attrs.get('animal')
        owner = attrs.get('owner')
        if animal.owner != owner:
            raise ValidationError('Only animal owner can perform this action')
        return super().validate(attrs)

    def validate_awarded_bid(self, awarded_bid):
        bids = self.instance.bid_set if self.instance else Bid.objects.none()

        if awarded_bid:
            if not bids.exists():
                raise ValidationError(f'No Bids found for {self.instance}.')

            if not bids.filter(id=awarded_bid.id).exists():
                raise ValidationError(f'Only Bids from {self.instance} can be awarded.')

        return awarded_bid
