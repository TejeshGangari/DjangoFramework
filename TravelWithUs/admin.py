from django.contrib import admin
from .models import Destination
from users.models import Customers

# Register your models here.

admin.site.register(Destination)
admin.site.register(Customers)