from django.contrib.auth.models import AbstractUser
from django.db import models


# Auction items
class User(AbstractUser):
    account_balance = models.DecimalField(decimal_places=2, max_digits=1000, blank=True, null=True)


class CatOrHedgehog(models.Model):
    breed = models.CharField(max_length=120)
    nickname = models.CharField(max_length=120)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nickname} ({self.breed})"


class Lot(models.Model):
    animal = models.ForeignKey(CatOrHedgehog, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True)
    awarded_bid = models.ForeignKey('base.Bid', on_delete=models.SET_NULL, default=None, blank=True, null=True)

    def __str__(self):
        return f"Lot {self.animal}. Price: {self.price}"


class Bid(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=1000)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # need to remove default=None
    related_lot = models.ForeignKey(Lot, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"Bid from {self.owner.username}"
