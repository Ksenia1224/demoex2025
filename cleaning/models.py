from django.db import models
from django.utils import timezone

from users.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Название услуги')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    phone = models.CharField(max_length=16, verbose_name='Телефон')
    date = models.DateTimeField(verbose_name='Дата и время', default=timezone.now)

    SERVICE_CHOICES = (
        ('general', 'Генеральная уборка'),
        ('clean', 'Общий клининг'),
        ('himch', 'Химчистка ковров и мебели'),
        ('poslestr', 'Послестроительная уборка'),
    )

    STATUS_CHOICES = (
        ('new', 'Новая'),
        ('in_progress', 'В процессе'),
        ('completed', 'Выполнено'),
        ('canceled', 'Отменено'),
    )

    PAYMENT_CHOICES = (
        ('card', 'Карта'),
        ('cash', 'Наличные')
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    service = models.CharField(max_length=20, choices=SERVICE_CHOICES, default='general')
    payment = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='card')
    cancel_reason = models.TextField(verbose_name='Причина отмены', blank=True, null=True)