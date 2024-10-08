from django.contrib import admin
from shop import models


# Register your models here.
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "role",
    )


@admin.register(models.Profile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "phone_number",
        "user",
    )


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
    )


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "status",
        "total_price",
    )


@admin.register(models.OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "product",
        "quantity",
        "price",
    )
