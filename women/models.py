from django.db import models
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id':self.pk})

    class Meta:
        ordering = ['-time_create']


class Category(models.Model):
    name = models.CharField(max_length=250)
    # women = models.ManyToManyField(Women, related_name='category', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
