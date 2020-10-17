from django.contrib import admin
from canteen_management_system import models
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(models.FoodItem)
admin.site.register(models.Cook)
admin.site.register(models.Employee)
admin.site.register(models.User, UserAdmin)