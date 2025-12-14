from django.db import models

Category_Choices = [
    ("movie", "Sinema Filmi"),
    ("series", "Dizi"),
    ("documentary", "Belgesel"),
]

class Movies(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    release_date = models.DateField(null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    poster = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=20, choices=Category_Choices, default="movie")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
