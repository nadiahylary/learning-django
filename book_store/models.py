from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestseller = models.BooleanField(default=False)
    slug = models.SlugField(default=" ", null=False, db_index=True)

    def __str__(self):
        return f"Title: {self.title} Rating: ({self.rating}) Author: {self.author} Bestseller?: {self.is_bestseller}"

    def get_absolute_url_id(self):
        return reverse("book-detail", args=[self.id])

    def absolute_url_slug(self):
        return reverse("book-detail-slug", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)