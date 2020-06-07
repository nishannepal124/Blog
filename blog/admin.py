from django.contrib import admin

# Register your models here.
from .models import Author, Post, Category


class PostViewAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'status','posted')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class AuthorViewAdmin(admin.ModelAdmin):
    list_display = ('author', 'description')
    list_filter = ("author",)
    search_fields = ['author', 'description']
    prepopulated_fields = {'description': ('author',)
    }

admin.site.register(Author, AuthorViewAdmin)
admin.site.register(Post, PostViewAdmin)
admin.site.register(Category)
