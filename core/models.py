from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Boleta(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Boletas'
    
    def __str__(self):
        return self.name
    
class Payment(models.Model):
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_due = models.DateField(null=True, blank=True)
    payment_day = models.DateField(null=True, blank=True)
    payed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.boleta.name} - {self.user.username}"