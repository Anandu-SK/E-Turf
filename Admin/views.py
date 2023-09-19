from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from Admin.models import *
from Manager.models import *
from User.models import *


# def adminindex(request):

#     return render(request, 'adminindex.html')


def admin_login(request):

    if request.method == 'POST':

        aemail = request.POST['aEmail']
        apassword = request.POST['aPassword']
        print(aemail, apassword)
        user = authenticate(request, username = aemail, password = apassword)

        

        if user is not None:
            login(request, user)
            
            return redirect('admindashboard')
        else:
            print("+++++++++++++++++++++++++++++++++++++++++++++++++")
            return redirect('admin_login')
    return render(request, 'admin_login.html')

def admin_logout(request):

        logout(request)
        return redirect('admin_login')


@login_required(login_url='admin_login')
def admindashboard(request):

    turf_count = Turflocation.objects.all().count()
    feedbackcount = Userfeedback.objects.all().count()
    manager_application_count = Managerregister.objects.filter(managerstatus=0).count()
    bookingrequests_count = Booknow.objects.filter(ubookingstatus=0).count()

    context = {

        'turf_count':turf_count, 'feedbackcount':feedbackcount,
        'manager_application_count':manager_application_count, 'bookingrequests_count':bookingrequests_count
    }

    return render(request, 'admindashboard.html', context)



def addturflocation(request):

    data = Districts.objects.all()

    if request.method == 'POST':

        tLocation = request.POST['tLocation']

        # tLocationDistrict = Districts.objects.get(districtname = tLocation)

        tName = request.POST['tName']

        tAddress = request.POST['tAddress']

        tPprice = request.POST['tPprice']

        tImage = request.FILES['tImage']

        tExtraimages = request.FILES.getlist('tExtraimages')

        if Turflocation.objects.filter(turfaddress = tAddress).exists():

            messages.warning(request,"This location already exists in the database")

        else:

            data = Turflocation.objects.create(turflocation = Districts.objects.get(id=tLocation), turfaddress = tAddress, turfimage = tImage, placeprice = tPprice, tname = tName )

            for images in tExtraimages:

                Extraimages.objects.create(location = data, additionalimages = images)

            return redirect('admindashboard')

    return render(request, 'addturflocation.html', {'data':data})




def viewallturfs(request):

    data = Turflocation.objects.all()

    data1 = Turfcategory.objects.all()

    context = {

        'data':data, 'data1':data1
    }

    return render(request, 'viewallturfs.html', context)




def viewindividual_turf_details(request, tId):

    data = Districts.objects.all()

    Turfdata = Turflocation.objects.filter(id=tId)

    Turfextraimages = Extraimages.objects.filter(location__id= tId)

    return render(request, 'updateturfdetails.html', {'Turfdata':Turfdata, 'Turfextraimages':Turfextraimages, 'data':data, "tId":tId})






def updateturflocation(request, lId):

    if request.method == 'POST':

        tLocation = request.POST['tLocation']

        tLocationDistrict = Districts.objects.get(id=tLocation)

        tName = request.POST['tName']

        tAddress = request.POST['tAddress']

        tPprice = request.POST['tPprice']

        try:

            tImage = request.FILES['tImage']

            fs = FileSystemStorage()

            files = fs.save(tImage.name, tImage)

        except MultiValueDictKeyError:

            files = Turflocation.objects.get(id=lId).turfimage

        data1 = Turflocation.objects.get(id=lId).id

        tExtraimages = request.FILES.getlist('tExtraimages')

        tExtraimageslist = []

        for i in tExtraimages:

            tExtraimageslist.append(i)

        

        # if Turflocation.objects.filter(turfaddress = tAddress).exists():

        #     messages.warning(request,"This TimeSlot for this date has been already booked")

        #     return redirect(f'/viewindividual_turf_details/{lId}' )

        # else:

        
        

        if len(tExtraimageslist) != 0:


            Extraimages.objects.filter(location__id = data1).delete()

            data = Turflocation(id=lId, turflocation = tLocationDistrict, turfaddress = tAddress, turfimage = files, placeprice = tPprice, tname = tName )

            data.save()

            for images in tExtraimages:

                print(images)

                Extraimages.objects.create(location = data, additionalimages = images)

            return redirect('viewallturfs')

           
        
        else:


            data = Turflocation(id = lId, turflocation = tLocationDistrict, turfaddress = tAddress, turfimage = files, placeprice = tPprice, tname = tName )

            data.save()


            return redirect('admindashboard')

            
        






def deleteturflocation(request, tId):

    Turflocation.objects.filter(id = tId).delete()

    return redirect('viewallturfs')
        



def turfcategory(request):

    if request.method == "POST":

        tCategory = request.POST['tCategory']

        tCprice = request.POST['tCprice']

        if Turfcategory.objects.filter(category = tCategory).exists():

            messages.warning(request,"This category already exists")

            return redirect('turfcategory')

        else:

            Turfcategory.objects.create(category = tCategory, categoryprice = tCprice)

            return redirect('admindashboard')

    return render(request, 'turfcategory.html')


def individual_turfcategory_view(request, tId):

    turf_category = Turfcategory.objects.filter(id = tId)

    return render(request, 'updateturfcategory.html', {'turf_category':turf_category})

def turfcategory_update(request, tId):

    if request.method == 'POST':

        tCategory = request.POST['tCategory']

        tCprice = request.POST['tCprice']

        Turfcategory.objects.filter(id = tId).update(category = tCategory, categoryprice = tCprice)

        return redirect('admindashboard')
    
def turfcategorydelete(request, tId):

    Turfcategory.objects.get(id=tId).delete()

    return redirect('viewallturfs')



def manager_tobe_approved_list(request):

    data = Managerregister.objects.filter(managerstatus = 0)

    data1 = Turflocation.objects.all()

    return render(request, 'managerapproval.html', {'data': data, 'data1':data1})




def managerapprove(request, mId):

    if request.method=='POST':

        mLocation = request.POST['mLocation']

        mLocation_instance = Turflocation.objects.get(id=mLocation)

        mLocation_instance_name = mLocation_instance.turfaddress

        if Managerregister.objects.filter(assignedturf = mLocation_instance).exists():

            messages.warning(request,"This Locations has been already assigned to a manager")
        
        else:

            Managerregister.objects.filter(id = mId).update(managerstatus = 1, assignedturf = mLocation_instance)

            manager_email = Managerregister.objects.get(id=mId).manageremail
            manager_name =  Managerregister.objects.get(id=mId).managerfname + " " + Managerregister.objects.get(id=mId).managerlname
            context = {'mLocation_instance_name':mLocation_instance_name,'manager_name':manager_name}
            
            template = render_to_string('automatedemail.html', context)
            email = EmailMessage(
                'Greetings',
                template,
                settings.EMAIL_HOST_USER,
                [manager_email],
            )
            email.fail_silently = False
            email.send()

        return redirect(reverse('manager_tobe_approved_list'))

def approved_managers_list(request):

    managerdata = Managerregister.objects.filter(managerstatus = 1)

    return render(request, 'approved_managers_list.html' ,{'managerdata':managerdata})

def delete_approved_managers(request, mId):

    Managerregister.objects.get(id=mId).delete()

    return redirect('approved_managers_list')
    

def managersrejected(request, mId):

    Managerregister.objects.filter(id = mId).update(managerstatus = 2)

    manager_email = Managerregister.objects.get(id=mId).manageremail
    manager_name =  Managerregister.objects.get(id=mId).managerfname + " " + Managerregister.objects.get(id=mId).managerlname
    context = {'manager_name':manager_name}
    
    template = render_to_string('managerrejectemail.html', context)
    email = EmailMessage(
        'Greetings',
        template,
        settings.EMAIL_HOST_USER,
        [manager_email],
    )
    email.fail_silently = False
    email.send()

    return redirect(reverse('manager_tobe_approved_list'))
    

def alluserfeedback(request):

    userfeedback = Userfeedback.objects.all()

    return render(request, 'alluserfeedback.html', {'userfeedback':userfeedback})


def adminallbookings(request):

    allbook = Booknow.objects.all()

    bookapprovelist = Booknow.objects.filter(ubookingstatus = 0)

    return render(request, 'allbookings.html', {'allbook':allbook, 'bookapprovelist':bookapprovelist})

def adminbookingapprove(request, bId):

    Booknow.objects.filter(id=bId).update(ubookingstatus = 1)

    return redirect('adminallbookings')




def admin_bill_generation(request, bId):

    booking_details = Booknow.objects.filter(id = bId)

    return render(request, 'admininvoice.html', {'booking_details':booking_details})


def admin_send_bill(request, sendbId):

    user_email = Booknow.objects.get(id=sendbId).ubookingemail
    user_name =  Booknow.objects.get(id=sendbId).ubookingname
    venue = Booknow.objects.get(id=sendbId).ubookingaddress
    category =  Booknow.objects.get(id=sendbId).ubookingcategory
    booked_date = Booknow.objects.get(id=sendbId).ubookingdate
    booked_time = Booknow.objects.get(id=sendbId).ubookingtime
    # payment_status = Booknow.objects.get(id=sendbId).upaymentstatus
    context = {'user_email':user_email, 'user_name':user_name, 'venue':venue, 'category':category, 'booked_date':booked_date, 'booked_time':booked_time}
    
    template = render_to_string('adminbillemail.html', context)
    email = EmailMessage(
        'Greetings',
        template,
        settings.EMAIL_HOST_USER,
        [user_email],
    )
    email.fail_silently = False
    email.send()
    return redirect('adminallbookings')


def adminbookingreject(request, bId):

    Booknow.objects.filter(id=bId).update(ubookingstatus = 2)

    user_email = Booknow.objects.get(id=bId).ubookingemail
    user_name =  Booknow.objects.get(id=bId).ubookingname
    turf_address = Booknow.objects.get(id = bId).ubookingaddress
    context = {'user_name':user_name, 'turf_address':turf_address }
    
    template = render_to_string('adminbookingrejectemail.html', context)
    email = EmailMessage(
        'Greetings',
        template,
        settings.EMAIL_HOST_USER,
        [user_email],
    )
    email.fail_silently = False
    email.send()

    return redirect(reverse('adminallbookings'))

