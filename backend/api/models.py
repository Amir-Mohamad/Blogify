from django.db import models
from django.contrib.auth import get_user_model
from django.utils.html import format_html
from ckeditor.fields import RichTextField
from .validators import validate_image


User = get_user_model()


class Category(models.Model):
    """
        All the articles have category,
        with OneToMany RelationShip
    """
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.title} created'


class Article(models.Model):
    """
        The main article model
    """
    STATUS_CHOICES = (
        ('d', 'draft'),
        ('p', "publish"),
    )
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = RichTextField()
    image = models.ImageField(upload_to='images/', validators=[validate_image])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, null=True)

    def __str__(self):
        return f'Article {self.title} created at {self.created}'

    # for showing the article image
    def cover(self):
        if self.image:
            return format_html("<img width=40 height=40 style='border-radius: 20px;' src='{}'>".format(self.image.url))
        return "nothing"
    cover.short_description = "cover"
