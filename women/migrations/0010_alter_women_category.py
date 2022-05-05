# Generated by Django 4.0.4 on 2022-04-30 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0009_alter_women_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='women', to='women.category', verbose_name='Рубрика'),
        ),
    ]