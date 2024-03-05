from django.contrib import admin
from .models import *



class NewsAdm(admin.ModelAdmin):
    search_fields = ('id','title','category','date','photo')
    list_display = ('title', 'date')
    list_filter = ('date', 'title', 'category')


admin.site.register(Cat_News)
admin.site.register(News,NewsAdm)