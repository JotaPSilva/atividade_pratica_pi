from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome=models.CharField(max_length=150)
    def __str__(self):
        return self.nome
    
class Filme(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    titulo = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return self.titulo

class Locacao(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    nome = models.CharField(max_length=150)
    data = models.DateField()
    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    def __str__(self):
        return self.nome