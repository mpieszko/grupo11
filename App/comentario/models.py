from django.db import models
from App.noticias.models import Noticia
from App.usuario.models import Usuario
from django.conf import settings


class Comentarios(models.Model):

    usuario         = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=Usuario)
    Noticia         = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    texto           = models.TextField(verbose_name='Comentario')
    fecha           = models.DateTimeField(auto_now_add=True)


def str(self):

        return self.texto

class Meta:

    ordering = ['-fecha']