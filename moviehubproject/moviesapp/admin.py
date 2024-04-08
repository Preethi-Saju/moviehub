from django.contrib import admin
from . models import Category,Movie


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class MovieAdmin(admin.ModelAdmin):
    list_display = ['name','date','actors']
    list_editable = ['date','actors']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20
admin.site.register(Movie,MovieAdmin)

