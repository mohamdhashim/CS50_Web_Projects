from django.contrib import admin
from auctions.models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Listings)
admin.site.register(Comments)
admin.site.register(Bids)
admin.site.register(Watch_List)
