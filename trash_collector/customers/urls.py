from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('weekly_pickup/', views.weekly_pickup, name='weekly_pickup'),
    path('bonus_pickup/', views.bonus_pickup, name='bonus_pickup'),
    path('create/', views.create, name='create'),
    path('balance/', views.balance, name='balance'),
    path('weekly_pickup', views.suspend_dates, name='suspend_dates'),
    path('details/', views.details, name='details')
]
