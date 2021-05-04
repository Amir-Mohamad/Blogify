from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    """
        All the articles have category,
        with OneToMany RelationShip
    """
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)


    def __str__(self):
        return f'{self.title} created'


class Article(models.Model):
    """
        The main article model
    """
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    upadted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Article {self.title} created at {self.created}'
