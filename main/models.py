from django.db import models

#? Модель БД для хранения мебели
class Furniture(models.Model):
  CATEGORY_CHOICES = [
    ('table', 'Table'),
    ('chair', 'Chair'),
    ('sofa', 'Sofa'),
  ]

  #? Поля в таблице БД
  name = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

  def __str__(self):
    return self.name

#? Моделт БД для создания заказа
class Order(models.Model):
  email = models.EmailField()
  items = models.ManyToManyField(Furniture, related_name='orders')
  total_price = models.DecimalField(max_digits=10, decimal_places=2)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"Заказ №{self.id}, email клиента: {self.email}"
