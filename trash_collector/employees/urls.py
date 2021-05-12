from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:customer_id>', views.charge_customer, name="charge_customer"),
    path('create/', views.create, name="create"),
    path('view_schedule/', views.view_schedule, name='view_schedule')
]
