from django.http import HttpResponse
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
    # if request.method == 'POST':
    #     current_customer = Customer.objects.get(pk=customer_id)
    #     current_customer.weekly_pickup = request.POST.get('weekly_pickup')
    #     current_customer.save()
    #     return render(request, 'customers/weekly_pickup.html')
    # else:
    #     current_customer = Customer.objects.get(pk=customer_id)
    #     context = {
    #         'weekly_pickup': current_customer
    #     }
    #     return render(request, 'customers/weekly_pickup.html', context)
    pass
    # current_customer = Customer.objects.get(pk=customer_id)
    # if current_customer.weekly_pickup is None:
    #
    # if request.method == 'POST':
    #     customer_weekly_pickup = Customer.objects.get('weekly_pickup')
    #     if customer_weekly_pickup ==
    #     return render(request, 'customers/weekly_pickup.html')
