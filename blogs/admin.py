from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . models import BlogCategory,Blog

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','author_name')


class BlogAdmin(admin.ModelAdmin):
    exclude=('Published_Date',)
    list_display =('author_name','title','category','description',)



admin.site.register(BlogCategory, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)

