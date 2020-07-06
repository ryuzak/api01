from django.db import models

# Create your models here.
class Marca(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')
    minimum_price = models.FloatField(default=0.00, verbose_name='Precio minimo')
    status = models.BooleanField(default=True, verbose_name='status')

    class Meta:
        db_table = 'Marcas'
        ordering = ['-created_date']