from django.db import models

# Create your models here.

class Ebook(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='thumbnails/')

    def __str__(self):
        return self.title
