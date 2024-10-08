from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "Администратор"),
        ("manager", "Менеджер"),
        ("customer", "Клиент"),
    )

    role = models.CharField(
        max_length=20, choices=ROLE_CHOICES, default="customer", verbose_name="Роль"
    )

    class Meta:
        ordering = ("username",)
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def is_admin(self):
        return self.role == "admin"

    def is_manager(self):
        return self.role == "manager"

    def is_customer(self):
        return self.role == "customer"

    def __str__(self) -> str:
        return super().__str__()


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, verbose_name="Пользователь"
    )
    phone_number = models.CharField(
        max_length=20, blank=True, verbose_name="Номер телефона"
    )
    avatar = models.ImageField(upload_to="", blank=True, verbose_name="Аватар")
    bio = models.TextField(blank=True, verbose_name="О себе")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return f"Профиль пользователя: {self.user.username}"


class Category(models.Model):
    name = models.CharField(verbose_name="Название", max_length=255)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Родительская категория",
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def get_all_children(self):
        children = []
        for category in Category.objects.filter(parent=self):
            children.append(category)
            children.extend(category.get_all_children())
        return children

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    category = models.ManyToManyField(
        Category,
        related_name="clothes",
        verbose_name="Категория",
        blank=False,
    )
    name = models.CharField(
        max_length=200,
        verbose_name="Название",
    )
    image = models.ImageField(upload_to="", blank=True, verbose_name="Фото")
    description = models.TextField(
        blank=True,
        verbose_name="Описание",
    )
    stock = models.PositiveIntegerField(default=0, verbose_name="На складе")
    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name="Цена",
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    class Meta:
        ordering = ("name",)
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def get_absolute_url(self):
        return f"/products/{self.id}/"

    def is_in_stock(self):
        return self.stock > 0

    def get_discount_price(self, discount=None):
        if discount:
            if discount.discount_type == "percentage":
                return self.price * (1 - discount.value / 100)
            elif discount.discount_type == "fixed":
                return self.price - discount.value
        return self.price

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=(
            ("processing", "В обработке"),
            ("shipped", "Отправлен"),
            ("completed", "Завершен"),
            ("canceled", "Отменен"),
        ),
        default="processing",
    )
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def get_items(self):
        return OrderItem.objects.filter(order=self)

    def get_total_price(self):
        total = 0
        for item in self.get_items():
            total += item.price * item.quantity
        return total

    def update_total_price(self):
        self.total_price = self.get_total_price()
        self.save()

    def __str__(self):
        return f"Заказ #{self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(
        max_length=4,
        choices=(
            ("XS", "XS"),
            ("S", "S"),
            ("M", "M"),
            ("L", "L"),
            ("XL", "XL"),
            ("XXL", "XXL"),
            ("XXXL", "XXXL"),
        ),
        verbose_name="Размер",
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Деталь заказа"
        verbose_name_plural = "Детали заказа"

    def get_total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
