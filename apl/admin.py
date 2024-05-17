from django.contrib import admin
from .models import *

class ComAdm(admin.ModelAdmin):
    search_fields = ('id','title','category','content')
    list_display = ('title', 'content')
    list_filter = ( 'title','content')

admin.site.register(Category)
admin.site.register(Post,ComAdm)
admin.site.register(Img)


