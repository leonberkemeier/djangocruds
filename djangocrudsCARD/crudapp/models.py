from django.db import models

# Create your models here.

class Cards(models.Model):
    front = models.CharField(max_length=100, verbose_name="FrontCard")
    back = models.CharField(max_length=100, verbose_name="BackCard")

    def __str__(self):
        return str(self.id)