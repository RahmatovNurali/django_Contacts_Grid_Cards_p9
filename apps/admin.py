from django.contrib import admin

from apps.models import Customer, Jobs, Address

admin.site.register(Customer)
admin.site.register(Jobs)
admin.site.register(Address)