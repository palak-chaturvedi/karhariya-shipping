import json
from datetime import timezone

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from homepage.models import *
import sweetify
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.

def homepage(request):
    return render(request, "home/homepage.html")


def service(request):
    return render(request, "home/service.html")

def about(request):
    return render(request, "home/about.html")

@csrf_exempt
def contact(request):
    if(request.method=="POST"):
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        subject = request.POST.get('subject','')
        message_text = request.POST.get('message','')
        # message = render_to_string('home/email_temp.html', data)
        # subject = "New Request for quotation"
        print(message_text)
        # message =  json.dumps(data)
        from_email = settings.EMAIL_HOST_USER
        print(from_email)
        message = f'''
        A message from {email} and {name}.
        {message_text}
'''

        receipt_list = ["palakchaturvedi_mc20a7_40@dtu.ac.in"]
        send_mail(subject, message, from_email, receipt_list)
        sweetify.success(request, "Sent Mail")

        return redirect("homepage")
    else:
        sweetify.error(request, "Mail not sent")
        return render(request, "home/contact.html")



def quotation(request):
    if(request.method == 'POST'):
        try:
            name=request.POST.get('name',0)
            email=request.POST.get('email',0)
            por=request.POST.get('por',0)
            pod=request.POST.get('pod',0)
            pol=request.POST.get('pol',0)
            fpod=request.POST.get('fpod',0)
            weight=request.POST.get('weight',0)
            cbm=request.POST.get('cbm',0)
            volume=request.POST.get('volume',0)
            hazard=request.POST.get('hazard',0)
            stackable=request.POST.get('stackable',0)
            quote = Quotation.objects.create(Name=name,
                                             Email=email,
                                             Pol=pol,
                                             Por=por,
                                             Pod=pod,
                                             FPod=fpod,
                                             Weight =weight,
                                             CBM = cbm,
                                             Volume = volume,
                                             Hazard=hazard,
                                             Stackable=stackable)
            print(quote)

            sweetify.success(request, "Email Sent")

            data = {
                "Name" : name,
            "Email" : email,
            'Pol' : pol,
            'Por' : por,
            'Pod' : pod,
            'FPod' : fpod,
            'Weight' : weight,
            'CBM' : cbm,
            'Volume' : volume,
            'Hazard' : hazard,
            'Stackable' : stackable
            }

            message = render_to_string('home/email_temp.html', data)
            subject = "New Request for quotation"
            # message =  json.dumps(data)
            from_email = settings.EMAIL_HOST_USER
            print(from_email)
            receipt_list = ["palakchaturvedi_mc20a7_40@dtu.ac.in"]
            send_mail(subject, message, from_email, receipt_list)
            sweetify.success(request, "Sent Mail")

            return redirect("homepage")
        except Exception as e:
            print(e)
            sweetify.error(request, e)

            return render(request, 'home/quotation.html')




    else:
        return render(request, "home/quotation.html")

@login_required(login_url = 'login')
def track(request):
    if(request.method=="POST"):
        trackingno = request.POST.get('trackid',0)
        type = request.POST.get('type', 0)
        if (type == "RO"):
            track = Track.objects.filter(RO=trackingno)
        elif (type == "HBL"):
            track = Track.objects.filter(HBL=trackingno)
        elif (type == "MWB"):
            track = Track.objects.filter(MWB=trackingno)
        elif (type == "AWB"):
            track = Track.objects.filter(AWB=trackingno)

        print(track)
        return render(request, 'home/track.html', {'track':track})
    else:
        return render(request, 'home/track.html')

@login_required(login_url='login')
def edit(request):
    if(request.user.is_superuser):
        if(request.method=='POST'):
            trackingno  = request.POST.get('trackidno',0)
            type = request.POST.get('type', 0)
            if(type=="RO"):
                track = Track.objects.filter(RO=trackingno)
            elif(type=="HBL"):
                track = Track.objects.filter(HBL=trackingno)
            elif(type=="MWB"):
                track = Track.objects.filter(MWB=trackingno)
            elif(type=="AWB"):
                track = Track.objects.filter(AWB=trackingno)
            context = {
                'track':track
            }
            return render(request, "home/edit.html", context)

        else:
            track = Track.objects.all()
            context = {
                'track': track
            }

            for item in track:
                print(item.Details)

            print(track)
            return render(request, "home/edit.html", context)


    else:
        sweetify.warning(request, "Only admin can access")
        return redirect('homepage')


def new_id(request):
    print("NEWWWW ")

    if(request.method=='POST'):
        ro = request.POST.get('trackid',0)
        awb = request.POST.get('AWB',0)
        hbl = request.POST.get('HBL',0)
        mbl = request.POST.get('MBL',0)
        GIGM = request.POST.get('GIGM',0)
        FC = request.POST.get('FC',0)
        CIGM = request.POST.get('CIGM',0)
        details = request.POST.get('details',0)
        track = Track.objects.create(RO = ro,
                                     AWB = awb,
                                     HBL = hbl,
                                     MBL = mbl,
                                     CIGM = CIGM,
                                     GIGM = GIGM,
                                     FC = FC,
                                     Details = details,
                                     )
        track.save()
        sweetify.success(request, "New id added successfuly")
        return redirect('edit')
    else:
        return render(request, 'home/new_id.html')


def edit_details(request, ro):
    if(request.method=='POST'):
        track = Track.objects.get(RO=ro)
        ro = request.POST.get('trackid', 0)
        awb = request.POST.get('AWB', 0)
        hbl = request.POST.get('HBL', 0)
        mbl = request.POST.get('MBL', 0)
        GIGM = request.POST.get('GIGM', 0)
        FC = request.POST.get('FC', 0)
        CIGM = request.POST.get('CIGM', 0)
        details = request.POST.get('details', 0)
        track.RO = ro
        track.AWB = awb
        track.HBL = hbl
        track.MBL = mbl
        track.GIGM = GIGM
        track.FC = FC
        track.CIGM = CIGM
        track.Details = details
        track.save()
        sweetify.success(request, "Edit Successful")
        return redirect('edit')
    else:
        track = Track.objects.get(RO=ro)
        print(track.Details)
        return render(request, 'home/edit_details.html', {'track':track})


def delete(request, ro):
    track = Track.objects.filter(RO=ro).delete()
    sweetify.success(request, f"Deleted RO number {ro} successfully")
    return redirect('edit')

    print(track)

    return HttpResponse("Hello")




