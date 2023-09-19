from django.urls import path
from Admin.views import *

urlpatterns = [
    path('admin_login/', admin_login,name='admin_login'),
    path('admin_logout/', admin_logout, name = 'admin_logout'),
    path('admindashboard/', admindashboard, name='admindashboard'),
    # path('managerapproval', managerregister, name='managerapproval'),
    path('addturflocation', addturflocation, name='addturflocation'),
    path('viewindividual_turf_details/<int:tId>', viewindividual_turf_details, name='viewindividual_turf_details'),
    path('updateturflocation/<int:lId>/', updateturflocation, name='updateturflocation'),
    path('deleteturflocation/<int:tId>/', deleteturflocation, name='deleteturflocation'),
    path('turfcategory', turfcategory, name='turfcategory'),
    path('individual_turfcategory_view/<int:tId>/', individual_turfcategory_view, name='individual_turfcategory_view'),
    path('turfcategory_update/<int:tId>/',turfcategory_update, name='turfcategory_update' ),
    path('turfcategorydelete/<int:tId>/', turfcategorydelete, name='turfcategorydelete'),
    path('manager_tobe_approved_list', manager_tobe_approved_list, name='manager_tobe_approved_list'),
    path('viewallturfs', viewallturfs, name='viewallturfs'),
    path('managerapprove/<int:mId>', managerapprove, name='managerapprove'),
    path('managersrejected/<int:mId>/',managersrejected, name='managersrejected'),
    path('alluserfeedback/', alluserfeedback, name='alluserfeedback'),
    path('adminallbookings', adminallbookings, name='adminallbookings'),
    path('adminbookingapprove/<int:bId>/', adminbookingapprove, name='adminbookingapprove'),
    path('adminbookingreject/<int:bId>/', adminbookingreject, name='adminbookingreject'),
    path('admin_bill_generation/<int:bId>/', admin_bill_generation, name='admin_bill_generation'),
    path('admin_send_bill/<int:sendbId>/', admin_send_bill, name='admin_send_bill'),
    path('approved_managers_list/', approved_managers_list, name='approved_managers_list'),
    path('delete_approved_managers/<int:mId>', delete_approved_managers, name='delete_approved_managers')
]