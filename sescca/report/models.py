from school.models import Student
from django.db import models
from school.models import Student

# Create your models here.

class Conduct(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    conduct = models.CharField(max_length=100, verbose_name='Conducta')

class DailyData(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    updated = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    daily_score = models.DecimalField(verbose_name='Promedio Diario', max_digits=5, decimal_places=2, default=000.00)

class WeeklyData(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    updated = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    weekly_score = models.DecimalField(verbose_name='Promedio Semana', max_digits=5, decimal_places=2, default=000.00)
