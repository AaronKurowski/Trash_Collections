from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from .models import Customer
# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user
    # It will be necessary while creating a customer/employee to assign the logged-in user as the user foreign key
    # This will allow you to later query the database using the logged-in user,
    # thereby finding the customer/employee profile that matches with the logged-in user.
    print(user)
    return render(request, 'customers/index.html')


def weekly_pickup(request):
    user = request.user
    customer = Customer.objects.get(user_id=user.id)
    if request.method == 'POST':
        customer.weekly_pickup = request.POST.get('weekly_pickup')
        customer.save()
    return render(request, 'customers/weekly_pickup.html')


def bonus_pickup(request):
    user = request.user
    customer = Customer.objects.get(user_id=user.id)
    if request.method == 'POST' and customer.bonus_pickup is None:
        customer.bonus_pickup = request.POST.get('bonus_pickup')
        customer.save()
    return render(request, 'customers/bonus_pickup.html')
