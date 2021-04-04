from django.contrib import admin
from .models import Product2,Offer

# admin
class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class Product2Admin(admin.ModelAdmin):  # customization of admin
    list_display = ('name', 'price', 'stock')


admin.site.register(Product2, Product2Admin)  # we have to manage our product2 in admin area
admin.site.register(Offer, OfferAdmin)

