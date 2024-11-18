from django.db import models
from django.contrib.auth.models import User


class Forum(models.Model):
    nome = models.CharField(max_length=255)
    topico = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='foruns',null=True)  # Adicione related_name
    datainicio = models.DateTimeField(auto_now_add=True)
    datatermino = models.DateTimeField(null=True, blank=True)

    def _str_(self):
        return self.nome

class Comentario(models.Model):
    forum = models.ForeignKey(Forum, related_name='comentarios', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios', null=True)  # Adicione related_name
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.user.first_name}: {self.texto}"