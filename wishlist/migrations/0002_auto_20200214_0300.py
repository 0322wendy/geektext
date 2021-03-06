# Generated by Django 3.0.2 on 2020-02-14 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0012_auto_20200204_2358'),
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='name',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='books',
            field=models.ManyToManyField(blank=True, to='details.Book'),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='listname',
            field=models.CharField(default='My Wishlist', max_length=20),
        ),
    ]
