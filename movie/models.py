from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Movie(models.Model):
    title = models.CharField(max_length=70)
    image = models.ImageField(upload_to='movie/images/')
    description = models.TextField(max_length=10000)
    actor1 = models.CharField(max_length=50)
    actor2 = models.CharField(max_length=50)
    actor3 = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})
