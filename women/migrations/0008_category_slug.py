# Generated by Django 4.0.3 on 2022-04-14 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0007_alter_women_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]