import random
import string

from django.contrib.auth import get_user_model
from django.db import models
from django.db.utils import IntegrityError
from django.utils import timezone


class CustomIDManager(models.Manager):

    def generate_unique_id(self):
        return ''.join(random.choices(string.digits, k=6))

    def create(self, *args, **kwargs):
        obj = None
        id = self.generate_unique_id()
        unique = False
        while not unique:
            try:
                obj = self.model(unique_id=id, *args, **kwargs)
                obj.save()
                unique = True
            except IntegrityError:
                id = self.generate_unique_id()
        return obj


class BidRoom(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(max_length=500, unique=True)
    description = models.TextField()
    starts_on = models.DateTimeField(default=timezone.now)
    ends_on = models.DateTimeField()
    initial_bid = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    obj = CustomIDManager()


class UserBid(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete='models.CASCADE', related_name='bids')
    room = models.ForeignKey(
        'sale.BidRoom', on_delete=models.CASCADE, related_name='user_bids')
    bid = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)