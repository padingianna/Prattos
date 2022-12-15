from django.db import models
from django.contrib.auth.models import User
from posts.models import Posteos

# Model

# Create your models here.
class Comment(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    profile = models.ForeignKey('users.Perfil', on_delete=models.PROTECT)
    post = models.ForeignKey(Posteos, on_delete=models.PROTECT)
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return self.comment 