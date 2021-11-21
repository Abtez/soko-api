from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(VendorProfile)
admin.site.register(Rating)
admin.site.register(Review)
admin.site.register(Wishlist)