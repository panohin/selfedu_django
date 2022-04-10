# Generated by Django 3.2.12 on 2022-04-10 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_alter_women_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('women', models.ManyToManyField(blank=True, related_name='category', to='women.Women')),
            ],
        ),
    ]
