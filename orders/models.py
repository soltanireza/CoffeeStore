import uuid

from django.db import models
from shop.models import Product

STATUS_CHOICES = (
    ('ordered', 'ordered'),
    ('confirmed', 'confirmed'),
    ('packed', 'packed'),
    ('posted', 'posted'),
    ('delivered', 'delivered'),
    )


class Order(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    unique_ID = models.CharField(primary_key=False, max_length=10, blank=True, unique=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=120, default='ordered', choices=STATUS_CHOICES)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # quantity = models.PositiveIntegerField(default=1)
    quantity = models.DecimalField(max_digits=3, decimal_places=1, default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
