from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(max_length=15, verbose_name='Текст')

    def __str__(self):
        return f'{self.title}, {self.text}'


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.CharField(max_length=340, verbose_name='Описание')
    article = models.ManyToManyField(Article, verbose_name='Статьи', null=True)

    def __str__(self):
        return f'{self.title}, {self.article}'