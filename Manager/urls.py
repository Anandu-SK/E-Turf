from django.urls import path
from Manager.views import *

urlpatterns = [

    path('managerregister', managerregister, name='managerregister'),
    path('login_for_all/', login_for_all, name='login_for_all'),
    path('logout_for_manager/', logout_for_manager, name='logout_for_manager'),
    path('logout_for_user/', logout_for_user, name='logout_for_user'),
    path('', index, name='index'),
    path('index/', index, name='about'),
    path('index/', index, name='contact'),
    path('managerindex', managerindex, name='managerindex'),
    path('managerdashboard', managerdashboard, name='managerdashboard'),
    path('managerwise_turfrates/',managerwise_turfrates, name='managerwise_turfrates'),
    path('userdashboard/',userdashboard, name='userdashboard'),
    path('bookingstable/', bookingstable, name='bookingstable'),
    path('bookingsapproved/<int:bId>/', bookingsapproved, name='bookingsapproved'),
    path('bookingsrejected/<int:bId>/', bookingsrejected, name='bookingsrejected'),
    path('managerwise_booking_history/', managerwise_booking_history, name='managerwise_booking_history'),
    path('bill_generation/<int:bId>/', bill_generation , name='bill_generation'),
    path('send_bill/<int:sendbId>/', send_bill, name='send_bill')
]