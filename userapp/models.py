from django.db import models

# Create your models here.
class User(models.Model):
    gender_choices = (
        (0, "男"),
        (1, "女"),
        (2, "未知"),
    )

    username = models.CharField(max_length=80)
    real_name = models.CharField(max_length=80)
    password = models.CharField(max_length=80)
    gender = models.SmallIntegerField(default=0, choices=gender_choices)
    status = models.SmallIntegerField(default=False)
    register_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "bz_user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username