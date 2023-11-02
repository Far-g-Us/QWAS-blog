from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=150, verbose_name='ФИО', blank=True, null=True)
    birth_date = models.DateField(verbose_name='Дата рождения', blank=True, null=True)


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(max_length=15, verbose_name='Текст')

    def __str__(self):
        return f'{self.title}, {self.text}'


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.CharField(max_length=340, verbose_name='Описание')
    article = models.ManyToManyField(Article, verbose_name='Статьи')

    def __str__(self):
        return f'{self.title}, {self.article}'