from django.db import models

class Park(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    city = models.CharField(max_length=100, verbose_name="Город")
    address = models.TextField(verbose_name="Адрес")
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    is_work = models.BooleanField(default=True, verbose_name="Работает")
    schedule = models.CharField(max_length=200, verbose_name="Расписание работы")
    def __str__(self):
        return f"{self.title} ({self.city})"
