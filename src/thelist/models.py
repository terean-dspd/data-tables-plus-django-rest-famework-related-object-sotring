from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(
        max_length=200
    )

    def __str__(self):
        return self.name

class Order(models.Model):
    amount = models.IntegerField(
        verbose_name="Amount"
    )
    item = models.CharField(
        max_length=200,
        verbose_name="Item"
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.PROTECT,
        verbose_name="Clent"
    )

    def __str__(self):
        return "Order {} {} {}".format(self.pk, self.item, self.amount)
