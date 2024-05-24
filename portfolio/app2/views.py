from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views.generic.base import View
from .forms import *
from django.contrib import auth
from django.contrib import messages
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from useraccount.decorators import login_required
# Create your views here.

@login_required
def index(request):
    return render(request, 'app2/index.html')


@login_required
def add_edit_About(request):
    instance = None
    try:
        if id:
            instance = About.objects.first()
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the About.')
        return redirect('dashboard:add_About')
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'About edited successfully.')
                return redirect('dashboard:add_About')  # Redirect to the added About's details page
            else:  # Add operation
                messages.success(request, 'About added successfully.')
                return redirect('dashboard:add_About')  # Redirect to the page for adding new Abouts
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = AboutForm(instance=instance)
    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_about.html', context)



def PersonalDetails(request):
    instance = None
    try:
        if id:
            instance = PersonalDetail.objects.first()
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the PersonalDetail.')
        return redirect('dashboard:add_PersonalDetails')
    if request.method == 'POST':
        form = PersonalDetailForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'PersonalDetail edited successfully.')
                return redirect('dashboard:add_PersonalDetails')  # Redirect to the edited PersonalDetail's details page
            else:  # Add operation
                messages.success(request, 'PersonalDetail added successfully.')
                return redirect('dashboard:add_PersonalDetails')  # Redirect to the page for adding new PersonalDetail
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = PersonalDetailForm(instance=instance)
    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_PersonalDetails.html', context)

@login_required 
def add_edit_Service(request, id=None):
    instance = None
    try:
        if id:
            instance = Service.objects.get(pk=id)
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the Service.')
        return redirect('dashboard:add_Service')
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'Service edited successfully.')
                return redirect('dashboard:edit_Service', id=instance.id)  # Redirect to the edited Service's details page
            else:  # Add operation
                messages.success(request, 'Service added successfully.')
                return redirect('dashboard:add_Service')  # Redirect to the page for adding new Services
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = ServiceForm(instance=instance)
    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_Service.html', context)

class ServiceListView(View):
    template_name = 'app2/Service.html'
    def get(self, request):
        prod = Service.objects.all()
   
        return render(request, self.template_name, {'details': prod})

class ServiceDeleteView(View):
    template_name = 'app2/Service.html'
    def get(self, request, id):
        record = get_object_or_404(Service, id=id)
        return render(request, self.template_name, {'details': record})
    def post(self, request, id):
        record = get_object_or_404(Service, id=id)
        record.delete()
        return redirect('dashboard:Service')

@login_required
def add_edit_Gallery(request, id=None):
    instance = None
    try:
        if id:
            instance = Gallery.objects.get(pk=id)
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the Gallery.')
        return redirect('dashboard:add_Gallery')
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'Gallery edited successfully.')
                return redirect('dashboard:edit_Gallery', id=instance.id)  # Redirect to the edited Gallery's details page
            else:  # Add operation
                messages.success(request, 'Gallery added successfully.')
                return redirect('dashboard:add_Gallery')  # Redirect to the page for adding new Gallerys
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = GalleryForm(instance=instance)
    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_Gallery.html', context)

class GalleryListView(View):
    template_name = 'app2/Gallery.html'
    def get(self, request):
        prod = Gallery.objects.all()
   
        return render(request, self.template_name, {'details': prod})

class GalleryDeleteView(View):
    template_name = 'app2/Gallery.html'
    def get(self, request, id):
        record = get_object_or_404(Gallery, id=id)
        return render(request, self.template_name, {'details': record})
    def post(self, request, id):
        record = get_object_or_404(Gallery, id=id)
        record.delete()
        return redirect('dashboard:Gallery')


@login_required 
def add_edit_Contact(request, id=None):
    instance = None
    try:
        if id:
            instance = Contact.objects.get(pk=id)
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the Contact.')
        return redirect('dashboard:add_Contact')
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'Contact edited successfully.')
                return redirect('dashboard:edit_Contact', id=instance.id)  # Redirect to the edited Contact's details page
            else:  # Add operation
                messages.success(request, 'Contact added successfully.')
                return redirect('dashboard:add_Contact')  # Redirect to the page for adding new Contacts
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = ContactForm(instance=instance)
    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_Contact.html', context)

class ContactListView(View):
    template_name = 'app2/Contact.html'
    def get(self, request):
        prod = Contact.objects.all()
   
        return render(request, self.template_name, {'details': prod})

class ContactDeleteView(View):
    template_name = 'app2/Contact.html'
    def get(self, request, id):
        record = get_object_or_404(Contact, id=id)
        return render(request, self.template_name, {'details': record})
    def post(self, request, id):
        record = get_object_or_404(Contact, id=id)
        record.delete()
        return redirect('dashboard:Contact')


# for logout
# def userlogout(request):
#     auth.logout(request)
#     messages.info(request, "logout successfully..")
#     return redirect('dashboard:signin')

# def signin(request):
#     return render(request,'app2/sign-in.html')




