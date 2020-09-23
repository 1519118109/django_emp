from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_name = models.CharField(max_length=80)
    img = models.ImageField(upload_to='pic', default="pic/1.jpg")
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    age = models.IntegerField()

    class Meta:
        db_table = "bz_employee"
        verbose_name = "员工"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.emp_name
