# Generated by Django 3.2.12 on 2022-04-10 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0003_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='category',
            name='women',
        ),
        migrations.AddField(
            model_name='women',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='women.category'),
        ),
    ]
