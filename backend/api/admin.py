from django.contrib import admin
from .models import Article, Category

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated', 'cover')
    list_filter = ('created', 'updated')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category)