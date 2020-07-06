from django.db import models

from marcas.models import Marca
from accounts.models import User

# Create your models here.
class Car(models.Model):
	name = models.CharField(max_length=50, verbose_name='Nombre')
	year = models.IntegerField(default=1950, verbose_name='Año')
	color = models.CharField(max_length=50, verbose_name='Color')
	fuel = models.FloatField(default=0.0, verbose_name='Combustible')
	status = models.BooleanField(default=True, verbose_name='status')
	brand = models.ForeignKey(Marca, verbose_name='Brands', on_delete=models.CASCADE, null=True)
	owner = models.ManyToManyField(User, verbose_name='user')
	def __str__(self):
		return self.name

	class Meta:
		db_table = 'cars'
		ordering = ['year', 'name']