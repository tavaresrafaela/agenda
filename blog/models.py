from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Cadastro(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telefone = models.CharField(max_length=50)
    aniversario = models.CharField(max_length=8)


    sexo_list = (
        ('0','Feminino'),
        ('1','Masculino'),
    )

    estado_list = (
        ('0', 'Solteiro'),
        ('1', 'Casado'),
    )
    sexo = models.CharField(max_length=1, choices=sexo_list)
    estado = models.CharField(max_length=1, choices=estado_list)

    def __str__(self):
        return self.nome
