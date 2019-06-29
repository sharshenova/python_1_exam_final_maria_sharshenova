from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=300, verbose_name="ФИО")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    death_date = models.DateField(null=True, blank=True, verbose_name="Дата смерти")
    bio = models.TextField(max_length=5000, null=True, blank=True, verbose_name="Биография")
    image = models.ImageField(upload_to='author_images', blank=True, null=True, verbose_name="Фото")
    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def get_absolute_url(self):
        return reverse('webapp:author_details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
