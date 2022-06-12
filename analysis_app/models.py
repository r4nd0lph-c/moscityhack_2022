from django.db import models


# Create your models here.


class Cities(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название города")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Название города"
        verbose_name_plural = "Названия городов"
        ordering = ["name"]
