from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Avg

class Book(models.Model):
    PURCHASE_CHOICES = [('New','New'),('Used','Used')]
    BOOK_TYPE = [('Hardback','Hardback'),('Paperback','Paperback')]
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    genre = models.CharField(max_length=30)
    condition = models.CharField(choices=PURCHASE_CHOICES, max_length=10, blank=True)
    type = models.CharField(choices=BOOK_TYPE, max_length=10)
    published_date=models.DateTimeField()
    cover = models.ImageField(upload_to='uploads/')
    cost = models.FloatField(null=True, blank=True, default=None)
    pages = models.IntegerField(null=True, blank=True, default=None)
    avg_rating = models.DecimalField(decimal_places=1, max_digits=2, default=0)

    def rating_avg(self):
        book = Book.objects.get(id=self.id)
        return list(book.rating_set.aggregate(Avg('rating')).values())[0]

    def rating_count(self):
        return Rating.objects.all().filter(book=self).count()
