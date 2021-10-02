from django.db import models

class Citacoes(models.Model):
    citacao = models.TextField()
    autor = models.CharField(max_length=150)