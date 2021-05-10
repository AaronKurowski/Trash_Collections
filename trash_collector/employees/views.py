from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps
from .models import Employee
import datetime
from datetime import date

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # Get the Customer model from the other app, it can now be used to query the db
    Customer = apps.get_model('customers.Customer')
    todays_customers = Customer.objects.filter(weekly_pickup=convert_todays_date_to_day()) | Customer.objects.filter(bonus_pickup=date.today())
    todays_customers = todays_customers.exclude(active=False)
    context = {'todays_customers': todays_customers}
    return render(request, 'employees/index.html', context)

def convert_todays_date_to_day():
    today = date.today()
    today = today.strftime("%A")
    return today

def set_active():
    # Function not complete
    Customer = apps.get_model('customers.Customer')
    todays_customers = Customer.objects.filter()
    for customer in todays_customers:
        if customer.suspend_start != None:
            if customer.suspend_start <= date.today() and customer.suspend_end >= date.today():
                customer.active = False
