from django.contrib import admin
from .models import Account, Admin, Guest, Staff

# Register your models here.

admin.site.register(Account)
admin.site.register(Admin)
admin.site.register(Guest)
admin.site.register(Staff)
