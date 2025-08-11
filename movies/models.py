from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)

    def __str__(self):
        return self.title