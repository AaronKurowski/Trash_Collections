from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50, default=None)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    active = models.BooleanField(default=False, blank=True, null=True)
    weekly_pickup = models.CharField(max_length=50, default=None, blank=True, null=True)
    bonus_pickup = models.DateField(auto_now=False, auto_now_add=False, default=None, blank=True, null=True)
    amount_due = models.DecimalField(max_digits=50, default=0, decimal_places=2, blank=True, null=True)

    zipcode = models.CharField(max_length=50, default=None, blank=True, null=True)
    address = models.CharField(max_length=50, default=None, blank=True, null=True)
    city = models.CharField(max_length=50, default=None, blank=True, null=True)
    phone_number = models.CharField(max_length=15, default=None, blank=True, null=True)

    last_completed = models.DateField(auto_now=False, auto_now_add=False, default=None, blank=True, null=True)
    suspend_start = models.DateField(auto_now=False, auto_now_add=False, default=None, blank=True, null=True)
    suspend_end = models.DateField(auto_now=False, auto_now_add=False, default=None, blank=True, null=True)

    def __str__(self):
        return self.name
