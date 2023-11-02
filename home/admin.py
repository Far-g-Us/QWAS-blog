from django.contrib import admin
from .models import Article, Book, CustomUser

# @admin.register(Article, Book)
admin.site.register(CustomUser)
admin.site.register(Article)
admin.site.register(Book)