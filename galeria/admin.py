from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "name","legend","visible")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_filter = ("category",)
    list_editable = ("visible",)
    list_per_page = 15

admin.site.register(Fotografia, ListandoFotografias)
