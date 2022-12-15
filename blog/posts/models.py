from django.db import models
from django.contrib.auth.models import User
from users.models import Perfil


class Posteos (models.Model):

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    perfil = models.ForeignKey('users.Perfil', on_delete=models.PROTECT)
    
    titulo = models.CharField(max_length=255)
    image_header = models.ImageField(upload_to='media/posts') 
    posteo = models.TextField(max_length=1000)

    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):

        return '{} by @{}'.format(self.titulo, self.user.username)