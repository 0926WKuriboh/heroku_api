from django.contrib import admin

# Register your models here.
from django.contrib import admin
from test1.models import Data
from test1.models import Source


class Data_Modeladmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'category', 'tag', 'display']


admin.site.register(Data, Data_Modeladmin)
admin.site.register(Source)
