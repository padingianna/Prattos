from django.contrib import admin

from posts.models import Posteos


@admin.register(Posteos)
class Posteos(admin.ModelAdmin):

    list_display = ('user', 'titulo', 'modificado')