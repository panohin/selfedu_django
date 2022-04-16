from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название статьи')
    content = models.TextField(blank=True, verbose_name='Содержание статьи')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, blank=True, null=True, verbose_name='Рубрика')
    slug = models.SlugField(max_length=255, null=True, blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title, allow_unicode=True)
            print(self.slug)
        super().save(*args, **kwargs)


    class Meta:
        ordering = ['-time_update']
        verbose_name = 'Женщины'
        verbose_name_plural = 'Известные женщины'


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name="Наименование рубрики")
    slug = models.SlugField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('by_category_url', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['id']
        verbose_name = "Рубрика"
        verbose_name_plural = "Рубрики"
