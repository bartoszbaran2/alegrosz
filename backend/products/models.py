from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    stock_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-price',)
        verbose_name_plural = 'Products'
        verbose_name = 'Products'
