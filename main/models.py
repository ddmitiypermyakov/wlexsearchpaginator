from django.db import models

# Create your models here.
class Trainig(models.Model):
    '''Модель'''
    # 1. Date, 2. Title, 3. Quantity, 4. Distance
    title = models.CharField('Название', max_length=255)
    quantity = models.PositiveIntegerField('Количество')
    distance = models.DecimalField('Расстояние', max_digits=8,decimal_places=2)
    date = models.DateField('Дата',auto_now_add=True)

    def __str__(self):
        return self.title