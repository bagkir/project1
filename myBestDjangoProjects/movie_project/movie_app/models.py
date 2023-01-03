from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.PositiveIntegerField()
    year = models.PositiveIntegerField(null=True)
    budjet = models.PositiveIntegerField(default=1000000)
    slug = models.SlugField(max_length=40, default='', null=True, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        # super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('movie-slug', args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.rating}'
