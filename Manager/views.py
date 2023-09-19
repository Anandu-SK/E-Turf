from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

from Admin.models import *
from Manager.models import *
from User.models import *


def managerregister(request):

    data = Districts.objects.all()

    if request.method == 'POST':

        mFname = request.POST['mFname']

        mLname = request.POST['mLname']

        mAddress = request.POST['mAddress']

        mCities = request.POST['mCities']

        mPhone = request.POST['mPhone']

        mEmail = request.POST['mEmail']

        mPassword = request.POST['mPassword']

        if Managerregister.objects.filter(manageremail = mEmail).exists():

            return render(request,'managerregistration.html', {'msg': 'This Email address already exists', 'data':data} )
        
        else:

            Managerregister.objects.create(managerfname = mFname, managerlname = mLname, manageraddress = mAddress, managercities = mCities, managerphone = mPhone, manageremail = mEmail, managerpassword = mPassword )

    return render(request, 'managerregistration.html', {'data':data})


def login_for_all(request):

    if 'u_id' in request.session:

        return redirect('userdashboard')
    
    elif 'm_id' in request.session:

        return redirect('managerdashboard')
    
    else:

        if request.method == 'POST':

            mEmail = request.POST['mEmail']

            mPassword = request.POST['mPassword']

            if Managerregister.objects.filter(manageremail = mEmail, managerpassword = mPassword).exists():

                data = Managerregister.objects.filter(manageremail = mEmail, managerpassword = mPassword).values('managerfname', 'managerlname', 'manageraddress', 'managercities', 'managerphone', 'managerstatus', 'id').first()
                
                if data['managerstatus'] == '0':

                    return render(request, 'login.html', {'msg1':"Your credentials are not approved by the admin Yet"} )
                else:
                    request.session['mfname'] = data['managerfname']
                    request.session['mlname'] = data['managerlname']
                    request.session['maddress'] = data['manageraddress']
                    request.session['mcities']  = data['managercities']
                    request.session['mphone'] = data['managerphone']
                    request.session['m_id'] = data['id']
                    request.session['mEmail'] = mEmail
                    request.session['mPassword'] = mPassword
                    return redirect('managerdashboard')
            
            
                
            elif Userregister.objects.filter(useremail = mEmail, userpassword = mPassword).exists():

                data = Userregister.objects.filter(useremail = mEmail, userpassword = mPassword).values('userfirstname', 'userlastname','userphone','id').first()

                request.session['ufname'] = data['userfirstname']
                request.session['ulname'] = data['userlastname']
                request.session['uphone'] = data['userphone']
                request.session['u_id'] = data['id']
                request.session['uEmail'] = mEmail
                request.session['uPassword'] = mPassword

                loginredirectsession = request.session.get('loginsession')


                if loginredirectsession is not None:

                    return redirect(loginredirectsession)

                else:

                    return redirect(reverse('userdashboard'))
                
            else:
                return render(request, 'login.html', {'msg':"Invalid Credentials"} )

        return render(request, 'login.html')
    
    

def logout_for_manager(request):

    del request.session['mfname']
    del request.session['mlname']
    del request.session['maddress']
    del request.session['mcities']
    del request.session['mphone']
    del request.session['m_id']
    del request.session['mEmail']
    del request.session['mPassword']

    return redirect('login_for_all')

def logout_for_user(request):

    del request.session['ufname']
    del request.session['ulname']
    del request.session['uphone']
    del request.session['u_id']
    del request.session['uEmail']
    del request.session['uPassword']

    if 'loginsession' in request.session:

        del request.session['loginsession']

    return redirect('login_for_all')


def index(request):
    return render(request, 'index.html')

def managerindex(request):
    return render(request, 'managerindex.html')

def managerdashboard(request):

    if 'm_id' in request.session:

        mid = request.session.get('m_id')
        managerinstance = Managerregister.objects.get(id = mid)
        managerturf = managerinstance.assignedturf
        booking_history = Booknow.objects.filter(ubookingaddress = managerturf).count()

        bookingrequests_count = Booknow.objects.filter(ubookingstatus = 0, ubookingaddress = managerturf).count()

        context = {

            'bookingrequests_count':bookingrequests_count, 'booking_history':booking_history

        }

        return render(request, 'managerdashboard.html', context)

    else:

        return redirect('login_for_all')


def managerwise_turfrates(request):

    if 'm_id' in request.session:

        managersession = request.session.get('m_id')

        data = Managerregister.objects.get(id=managersession)

        turfid = data.assignedturf.id

        turfdetails = Turflocation.objects.filter(id = turfid)

    turfcategorydetails = Turfcategory.objects.all()

        # TurfAmount = turfrate.placeprice

        # print(TurfAmount)

    return render(request, 'managerwise_turfrates.html', {'turfdetails': turfdetails, 'turfcategorydetails': turfcategorydetails})


def userdashboard(request):

    return render(request, 'userdashboard.html')


def bookingstable(request):

    if 'm_id' in request.session:

        managersession_id = request.session.get('m_id')

        manager_id = Managerregister.objects.get(id = managersession_id)

        Turf_location = manager_id.assignedturf

        bookings_tobe_approved = Booknow.objects.filter(ubookingstatus = 0, ubookingaddress = Turf_location)

    return render(request, 'bookingrequests.html', {'bookings_tobe_approved':bookings_tobe_approved})

def bookingsapproved(request, bId):

    Booknow.objects.filter(id = bId).update(ubookingstatus = 1)

    return redirect('bookingstable')


def managerwise_booking_history(request):

    if 'm_id' in request.session:

        managersession = request.session.get('m_id')

        managerid = Managerregister.objects.get(id=managersession)

        Turfassigned = managerid.assignedturf

        bookinghistory = Booknow.objects.filter(ubookingaddress = Turfassigned)

        return render(request, 'bookinghistory.html', {'bookinghistory':bookinghistory})
    

def bill_generation(request, bId):

    booking_details = Booknow.objects.filter(id = bId)

    return render(request, 'invoice.html', {'booking_details':booking_details})

def send_bill(request, sendbId):

    user_email = Booknow.objects.get(id=sendbId).ubookingemail
    user_name =  Booknow.objects.get(id=sendbId).ubookingname
    venue = Booknow.objects.get(id=sendbId).ubookingaddress
    category =  Booknow.objects.get(id=sendbId).ubookingcategory
    booked_date = Booknow.objects.get(id=sendbId).ubookingdate
    booked_time = Booknow.objects.get(id=sendbId).ubookingtime
    context = {'user_email':user_email, 'user_name':user_name, 'venue':venue, 'category':category, 'booked_date':booked_date, 'booked_time':booked_time}
    
    template = render_to_string('billemail.html', context)
    email = EmailMessage(
        'Greetings',
        template,
        settings.EMAIL_HOST_USER,
        [user_email],
    )
    email.fail_silently = False
    email.send()
    return redirect('managerwise_booking_history')

def bookingsrejected(request, bId):

    Booknow.objects.filter(id =bId).update(ubookingstatus = 2)

    user_email = Booknow.objects.get(id=bId).ubookingemail
    user_name =  Booknow.objects.get(id=bId).ubookingname
    turf_address = Booknow.objects.get(id = bId).ubookingaddress
    context = {'user_name':user_name, 'turf_address':turf_address }
    
    template = render_to_string('managerbookingrejectemail.html', context)
    email = EmailMessage(
        'Greetings',
        template,
        settings.EMAIL_HOST_USER,
        [user_email],
    )
    email.fail_silently = False
    email.send()

    return redirect('bookingstable')