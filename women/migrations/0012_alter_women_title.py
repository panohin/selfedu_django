# Generated by Django 4.0.4 on 2022-04-30 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0011_alter_women_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название статьи'),
        ),
    ]