from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    image = models.FilePathField(path="/img")

    def __str__(self):
        return self.title
