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


@login_required 
def add_edit_Testimonial(request, id=None):
    instance = None
    try:
        if id:
            instance = Testimonial.objects.get(pk=id)
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the Testimonial.')
        return redirect('dashboard:add_Testimonial')
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'Testimonial edited successfully.')
                return redirect('dashboard:edit_Testimonial', id=instance.id)  # Redirect to the edited Testimonial's details page
            else:  # Add operation
                messages.success(request, 'Testimonial added successfully.')
                return redirect('dashboard:add_Testimonial')  # Redirect to the page for adding new Testimonials
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = TestimonialForm(instance=instance)
    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_Testimonial.html', context)

class TestimonialListView(View):
    template_name = 'app2/Testimonial.html'
    def get(self, request):
        prod = Testimonial.objects.all()
   
        return render(request, self.template_name, {'details': prod})

class TestimonialDeleteView(View):
    template_name = 'app2/Testimonial.html'
    def get(self, request, id):
        record = get_object_or_404(Testimonial, id=id)
        return render(request, self.template_name, {'details': record})
    def post(self, request, id):
        record = get_object_or_404(Testimonial, id=id)
        record.delete()
        return redirect('dashboard:Testimonial')




@login_required 
def add_edit_Appointment(request, id=None):
    instance = None
    try:
        if id:
            instance = Appointment.objects.get(pk=id)
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the Appointment.')
        return redirect('dashboard:add_Appointment')
    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'Appointment edited successfully.')
                return redirect('dashboard:edit_Appointment', id=instance.id)  # Redirect to the edited Appointment's details page
            else:  # Add operation
                messages.success(request, 'Appointment added successfully.')
                return redirect('dashboard:add_Appointment')  # Redirect to the page for adding new Appointments
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = AppointmentForm(instance=instance)
    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_Appointment.html', context)

class AppointmentListView(View):
    template_name = 'app2/Appointment.html'
    def get(self, request):
        prod = Appointment.objects.all()
   
        return render(request, self.template_name, {'details': prod})

class AppointmentDeleteView(View):
    template_name = 'app2/Appointment.html'
    def get(self, request, id):
        record = get_object_or_404(Appointment, id=id)
        return render(request, self.template_name, {'details': record})
    def post(self, request, id):
        record = get_object_or_404(Appointment, id=id)
        record.delete()
        return redirect('dashboard:Appointment')

@login_required 
def create_or_edit_album(request, album_id=None):
    if album_id:
        album_instance = get_object_or_404(Album, id=album_id)
        GalleryFormSet = inlineformset_factory(Album, Gallery, form=GalleryForm, extra=1)
    else:
        album_instance = Album()
        GalleryFormSet = inlineformset_factory(Album, Gallery, form=GalleryForm,extra=1)
    if request.method == 'POST':
        album_form = AlbumForm(request.POST,request.FILES, instance=album_instance)
        formset = GalleryFormSet(request.POST,request.FILES, instance=album_instance)
        if album_form.is_valid() and formset.is_valid():
            album_instance = album_form.save()
            formset.instance = album_instance
            formset.save()
            if album_id:
                messages.success(request, 'Album Updated successfully.')
                return redirect('dashboard:edit_Album', album_id=album_instance.id)
            else:
                messages.success(request, 'Album added successfully.')
                return redirect('dashboard:add_Album')
    else:
        album_form = AlbumForm(instance=album_instance)
        formset = GalleryFormSet(instance=album_instance)
    context = {
        'album_form': album_form,
        'formset': formset,
        'is_inline_formset_used': True,
    }
    return render(request, 'app2/create_Album.html', context)


class AlbumListView(View):
    template_name = 'app2/Album.html'
    def get(self, request):
        prod = Album.objects.all()
        return render(request, self.template_name, {'details': prod})

class AlbumDeleteView(View):
    template_name = 'app2/Album.html'
    def get(self, request, id):
        record = get_object_or_404(Album, id=id)
        return render(request, self.template_name, {'details': record})
    def post(self, request, id):
        record = get_object_or_404(Album, id=id)
        record.delete()
        return redirect('dashboard:Album')


@login_required 
def add_edit_CompanyDescription(request, id=None):
    instance = None
    try:
        if id:
            instance = CompanyDescription.objects.get(pk=id)
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the CompanyDescription.')
        return redirect('dashboard:add_CompanyDescription')
    if request.method == 'POST':
        form = CompanyDescriptionForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'CompanyDescription edited successfully.')
                return redirect('dashboard:edit_CompanyDescription', id=instance.id)  # Redirect to the edited CompanyDescription's details page
            else:  # Add operation
                messages.success(request, 'CompanyDescription added successfully.')
                return redirect('dashboard:add_CompanyDescription')  # Redirect to the page for adding new CompanyDescriptions
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = CompanyDescriptionForm(instance=instance)
    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_CompanyDescription.html', context)

class CompanyDescriptionListView(View):
    template_name = 'app2/CompanyDescription.html'
    def get(self, request):
        prod = CompanyDescription.objects.all()
   
        return render(request, self.template_name, {'details': prod})

class CompanyDescriptionDeleteView(View):
    template_name = 'app2/CompanyDescription.html'
    def get(self, request, id):
        record = get_object_or_404(CompanyDescription, id=id)
        return render(request, self.template_name, {'details': record})
    def post(self, request, id):
        record = get_object_or_404(CompanyDescription, id=id)
        record.delete()
        return redirect('dashboard:CompanyDescription')


@login_required 
def HeroBanners(request):
    instance = None
    try:
        if id:
            instance = Herobanner.objects.first()
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the HeroBanner.')
        return redirect('dashboard:HeroBanner')
    if request.method == 'POST':
        form = HerobannerForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'HeroBanner edited successfully.')
                return redirect('dashboard:add_HeroBanner')  # Redirect to the edited HeroBanner's details page
            else:  # Add operation
                messages.success(request, 'HeroBanner added successfully.')
                return redirect('dashboard:add_HeroBanner')  # Redirect to the page for adding new HeroBanner
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = HerobannerForm(instance=instance)
    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_HeroBanner.html', context)









# for logout
# def userlogout(request):
#     auth.logout(request)
#     messages.info(request, "logout successfully..")
#     return redirect('dashboard:signin')

# def signin(request):
#     return render(request,'app2/sign-in.html')




