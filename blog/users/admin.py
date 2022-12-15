from django.contrib import admin

from users.models import Perfil


@admin.register(Perfil)
class Perfil(admin.ModelAdmin):

    list_display = ('user', 'descripcion', 'photo', 'date_modified')