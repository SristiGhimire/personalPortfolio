from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.core.mail import send_mail
from django.conf import settings 
from django.contrib.auth.models import User
from .forms import *


def index(request):
    contact = Contact.objects.all()
    about = About.objects.first()
    album = Album.objects.all()
    personaldetail = PersonalDetail.objects.first()
    service = Service.objects.all()
    testimonial = Testimonial.objects.all()
    company = CompanyDescription.objects.all()
    herobanner = Herobanner.objects.first()
    context = {"contact":contact, "about":about, "album":album, "personaldetail": personaldetail, "service": service, "testimonial":testimonial, "company": company, "herobanner": herobanner}
    return render(request, 'app/index.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST['email']
        message = request.POST['message']
        subject = request.POST['subject']
        contact_obj = Contact(name = name, email = email, message = message, subject=subject)
        contact_obj.save()
        
        # send mail with customer query
        email_subject = subject
        message =f"User Name : {name} \nmessage : {message}"
        email_from = settings.EMAIL_HOST_USER
        user_email = [email]
        send_mail(subject, message, email_from, user_email)
        return redirect('app:index') 
    else:
        return render(request, 'app/index.html')


def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:index')
    else:
        form = AppointmentForm()
    return render(request, 'app/index.html', {'form': form})






