from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    publication_date = models.DateField()
    source = models.CharField(max_length=100)
    url = models.URLField()
    category = models.CharField(max_length=100)
