from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps
from .models import Employee
import datetime
from datetime import date

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    user = request.user
    employee = Employee.objects.get(user_id=user.id)
    Customer = apps.get_model('customers.Customer')
    todays_customers = Customer.objects.filter(zipcode=employee.zipcode)
    todays_customers = todays_customers.filter(weekly_pickup=convert_todays_date_to_day()) | todays_customers.filter(bonus_pickup=date.today())
    todays_customers = set_active(todays_customers)
    todays_customers = todays_customers.exclude(active=False)
    context = {'todays_customers': todays_customers}
    return render(request, 'employees/index.html', context)

def convert_todays_date_to_day():
    today = date.today()
    today = today.strftime("%A")
    return today

def set_active(query_set):
    todays_customers = query_set
    for customer in todays_customers:
        if customer.suspend_start != None:
            if customer.suspend_start <= date.today() and customer.suspend_end >= date.today():
                customer.active = False
                customer.save()
            else:
                customer.active = True
                customer.save()
    return todays_customers
