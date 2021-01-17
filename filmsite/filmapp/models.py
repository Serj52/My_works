from django.db import models

class Producer(models.Model):

    producer_name = models.CharField(verbose_name='Имя', max_length=50, unique=True)
    age = models.PositiveIntegerField(verbose_name= 'Возраст', default=0)
    country = models.CharField(verbose_name= 'Страна', max_length=50)

    def __str__(self):
        return self.producer_name

class Film(models.Model):

    name = models.CharField(verbose_name='Название', max_length=50)
    genre = models.CharField(verbose_name='Жанр', max_length=50)
    year = models.CharField(verbose_name='Год', max_length=4)
    producer_name = models.ForeignKey(Producer, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
         return self.name




# Create your models here.
