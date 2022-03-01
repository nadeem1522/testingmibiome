from django.contrib import admin

from .models import BidRoom, UserBid


admin.site.register(BidRoom)
admin.site.register(UserBid)