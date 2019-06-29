from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=300, verbose_name="ФИО")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    death_date = models.DateField(null=True, blank=True, verbose_name="Дата смерти")
    bio = models.TextField(max_length=5000, null=True, blank=True, verbose_name="Биография")
    image = models.ImageField(upload_to='author_images', blank=True, null=True, verbose_name="Фото")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
