from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Customer Name")
    email = models.EmailField(max_length=277, verbose_name="Customer Email")

    def __str__(self):
        return str(self.id)