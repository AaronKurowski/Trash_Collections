from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    weekday_pickup = models.CharField(max_length=50)
    bonus_pickup = models.DateField(auto_now=False, auto_now_add=False)
    amount_due = models.DecimalField(max_digits=None, decimal_places=2)
