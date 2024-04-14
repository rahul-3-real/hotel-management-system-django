from django.contrib import admin
from .models import Account, Admin, Guest, Staff, JobPosition, Salary

# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = ("email", "type")
    list_filter = ("type",)


admin.site.register(Account, AccountAdmin)
admin.site.register(Admin)
admin.site.register(Guest)
admin.site.register(Staff)
admin.site.register(JobPosition)
admin.site.register(Salary)
