from django.db import models


from django.db import models
from library.models import Books

class ShoppingCart(models.Model):
    STATUS_CHOICES = (
        ("In Cart", "In Cart"),
        ("Purchased", "Purchased"),
        ("Removed", "Removed"),
    )
    item = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)
    related_book = models.ForeignKey(Books, on_delete=models.CASCADE)  # Связь с фильмами
    quantity = models.PositiveIntegerField(default=1)  # Количество товара
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.item} - {self.status} - Quantity: {self.quantity}'

