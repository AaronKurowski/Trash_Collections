from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50, default=None)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    weekly_pickup = models.CharField(max_length=50, default=None)
    bonus_pickup = models.DateField(auto_now=False, auto_now_add=False, default=None)
    amount_due = models.DecimalField(max_digits=50, default=0, decimal_places=2)

    zipcode = models.IntegerField(default=None)
    address = models.CharField(max_length=50, default=None)
    city = models.CharField(max_length=50, default=None)
    phone_number = models.CharField(max_length=15, default=None)

    last_completed = models.DateField(auto_now=False, auto_now_add=False, default=None)
    suspend_start = models.DateField(auto_now=False, auto_now_add=False, default=None)
    suspend_end = models.DateField(auto_now=False, auto_now_add=False, default=None)
