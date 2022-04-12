from django.db import models
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название статьи')
    content = models.TextField(blank=True, verbose_name='Содержание статьи')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, blank=True, null=True, verbose_name='Рубрика')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id':self.pk})

    class Meta:
        ordering = ['-time_update']
        verbose_name = 'Женщины'
        verbose_name_plural = 'Известные женщины'


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name="Наименование рубрики")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('by_category_url', kwargs={'cat_id':self.pk})

    class Meta:
        ordering = ['id']
        verbose_name = "Рубрика"
        verbose_name_plural = "Рубрики"
