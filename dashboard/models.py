from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer_name} - {self.movie.title}"