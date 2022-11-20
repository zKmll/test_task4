from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50)
    stripe_product_id = models.CharField(max_length=100)
    description = models.TextField(max_length=150)
    price = models.IntegerField(default=0)  # центы
    stripe_price_id = models.CharField(max_length=100)
    product = models.ForeignKey(name, stripe_product_id, on_delete=models.CASCADE)

    def __str__(self):
        return self.description, self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)  #перевод в доллары

    