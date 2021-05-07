from django.db import models


# TODO: Create an Employee model with properties required by the user stories

class Employee(models.Model):
    name = models.CharField(max_length=50, default=None)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)

    zipcode = models.IntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name
