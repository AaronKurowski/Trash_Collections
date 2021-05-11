from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render
from .models import Customer
from django.urls import reverse
# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    user = request.user
    try:
        customer = Customer.objects.get(user_id=user.id)
        context = {
            'customer': customer
        }
        return render(request, 'customers/index.html', context)
    except:
        return HttpResponseRedirect(reverse('customers:create'))


def weekly_pickup(request):
    user = request.user
    customer = Customer.objects.get(user_id=user.id)
    if request.method == 'POST':
        customer.weekly_pickup = request.POST.get('weekly_pickup')
        customer.save()
    return render(request, 'customers/weekly_pickup.html')


def suspend_dates(request):
    user = request.user
    customer = Customer.objects.get(user_id=user.id)
    if request.method == 'POST':
        customer.suspend_start = request.POST.get('suspend_start')
        customer.suspend_end = request.POST.get('suspend_end')
        customer.save()
    return render(request, 'customers/weekly_pickup.html')


def bonus_pickup(request):
    user = request.user
    customer = Customer.objects.get(user_id=user.id)
    if request.method == 'POST' and customer.bonus_pickup is None:
        customer.bonus_pickup = request.POST.get('bonus_pickup')
        customer.save()
    return render(request, 'customers/bonus_pickup.html')


def balance(request):
    user = request.user
    customer = Customer.objects.get(user_id=user.id)
    context = {
        'customer': customer
    }
    return render(request, 'customers/balance.html', context)


def create(request):
    user = request.user
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        zipcode = request.POST.get('zipcode')
        phone_number = request.POST.get('phone_number')

        new_customer = Customer(name=name, user_id=user.id, address=address, city=city, zipcode=zipcode,
                                phone_number=phone_number)
        new_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/create.html')


def details(request):
    user = request.user
    customer = Customer.objects.get(user_id=user.id)
    context = {
        'customer': customer
    }
    return render(request, 'customers/details.html', context)
