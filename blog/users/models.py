from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):

    user = models.OneToOneField(User, on_delete=models.PROTECT)

    descripcion = models.CharField(max_length=200, blank=True)

    photo = models.ImageField(
        upload_to='media/users',
        blank=True,
        null=True
    )

    date_modified = models.DateTimeField(auto_now=True) 


    def __str__(self):
        
        return self.user.username
        
        