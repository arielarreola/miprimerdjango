from django.db import models

# Create your models here.
class Comida(models.Model):
    nombre=models.CharField(max_length=30)
    calorias=models.IntegerField()
    origen=models.CharField(max_length=30)
    ingredientes=models.TextField()
    creado=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre} {self.creado}"
    
class Bebida(models.Model):
    nombre=models.CharField(max_length=30)
    sabor=models.CharField(max_length=30)
    alcoholica=models.BooleanField()
    cantidadml=models.IntegerField()
    creado=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.nombre} {self.creado}"