from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


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


class Book(models.Model):
    title = models.CharField(max_length=300, verbose_name="Название книги")
    author = models.ForeignKey(Author, related_name="books", verbose_name="Автор", on_delete=models.CASCADE)
    published_at = models.CharField(max_length=6, verbose_name="Год издания")
    file = models.FileField(upload_to='book_files', blank=True, null=True, verbose_name="Файл")
    image = models.ImageField(upload_to='book_images', blank=True, null=True, verbose_name="Обложка")
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('webapp:book_details', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class Review(models.Model):
    text = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Отзыв")
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name="reviews", blank=True, verbose_name="Книга", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True, verbose_name="Дата-время создания")

    def get_absolute_url(self):
        return reverse('webapp:book_details', kwargs={'pk': self.book.id})

    def __str__(self):
        return f"{self.pk}. {self.text} | {self.author.username}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
