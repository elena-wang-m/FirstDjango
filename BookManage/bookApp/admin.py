from django.contrib import admin
# Register your models here.
from .models import Book, Hero

class HeroInline(admin.TabularInline):
    model = Hero
    extra = 2

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_date']
    list_filter = ['title', 'pub_date']
    search_fields = ['title']
    list_per_page = 3
    inlines = [HeroInline]

class HeroAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'sex', 'content', 'Book']
    list_filter = ['Book']
    search_fields = ['name']
    list_per_page = 10

# 后台管理的配置文件
# Register your models here.
admin.site.register(Book,BookAdmin)
admin.site.register(Hero,HeroAdmin)