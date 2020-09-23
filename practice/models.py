from django.db import models

# Create your models here.
class Computer(models.Model):
    computer_name = models.CharField(max_length=80, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    brand = models.CharField(max_length=16, verbose_name="品牌")

    class Meta:
        db_table = "bz_computer"
        verbose_name = "电脑"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.computer_name