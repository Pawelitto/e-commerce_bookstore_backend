from django.db import models

# Create your models here.

class books(models.Model):
    isbn13 = models.CharField(max_length=13)
    isbn10 = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, null=True)
    authors = models.CharField(max_length=100, null=True)
    categories = models.CharField(max_length=100, null=True)
    thumbnail = models.CharField(max_length=500, null=True)
    description = models.CharField(max_length=6000, null=True)
    published_year = models.CharField(max_length=4, null=True)
    average_rating = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    num_pages = models.IntegerField(primary_key=False, null=True)
    ratings_count = models.IntegerField(primary_key=False, null=True)

    def __str__(self):
        return self.title

