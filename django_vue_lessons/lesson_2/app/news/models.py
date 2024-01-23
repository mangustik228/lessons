from django.db import models

# Create your models here.


class Journalist(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=150)
    biography = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Article(models.Model):
    # author = models.CharField(max_length=120)
    author = models.ForeignKey(
        Journalist,
        on_delete=models.CASCADE,
        related_name="articles")
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField(null=True)
    location = models.CharField(max_length=120)
    publication_date = models.DateField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}[{self.author}]"
