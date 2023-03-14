from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.name} ({self.code.upper()})"

    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street = models.CharField(max_length=80)
    zip_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.zip_code}, {self.city}"

    class Meta:
        verbose_name_plural = "Addresses"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.SET("None"), null=True)

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    # author = models.CharField(null=True, max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True,
                               related_name="books")
    is_bestseller = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True,
                            null=False, db_index=True)
    countries_published_in = models.ManyToManyField(Country)

    def __str__(self):
        return f"Title: {self.title} Rating: ({self.rating}) Author: {self.author} Bestseller?: {self.is_bestseller}"

    def get_absolute_url_id(self):
        return reverse("book-detail", args=[self.id])

    def absolute_url_slug(self):
        return reverse("book-detail-slug", args=[self.slug])

    def save(self, *args, **kwargs):
        """not really need anymore because the slug field is being
     automatically prepopulated in the admin interface"""
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

