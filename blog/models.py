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
    nome = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    idade = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telefone = models.CharField(max_length=50)
    aniversario = models.CharField(max_length=3)
    datea = models.CharField(max_length=15)

    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    sexo = {
        ('0','Feminino'),
        ('1','Masculino'),
    }

    estado = {
        ('0', 'Solteiro'),
        ('1', 'Casado'),
    }

    def __str__(self):
        return self.title
