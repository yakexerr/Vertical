from django.db import models

class Park(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    city = models.CharField(max_length=100, verbose_name="Город")
    address = models.TextField(verbose_name="Адрес")
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    is_work = models.BooleanField(default=True, verbose_name="Работает")
    schedule = models.CharField(max_length=200, verbose_name="Расписание работы")
    main_photo = models.ImageField(
        verbose_name='Главное фото',
        upload_to='parks/',
        blank=True,
        null=True
    )
    def __str__(self):
        return f"{self.title} ({self.city})"

class Entertainment(models.Model):
    park = models.ForeignKey(Park, on_delete=models.CASCADE, verbose_name="Парк")
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    min_height = models.CharField(max_length= 50, verbose_name="Минимальный рост")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")
    def __str__(self):
        return f"{self.title} ({self.park.title}, {self.description})"