from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField  (upload_to='product/%Y/%m/%d/', blank=True)
    photo_1 = models.ImageField(upload_to='product/%y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='product/%y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='product/%y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='product/%y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='product/%y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='product/%y/%m/%d/', blank=True)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
