from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, CatOrHedgehog, Lot, Bid

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(CatOrHedgehog)
admin.site.register(Lot)
admin.site.register(Bid)
