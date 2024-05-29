from django.urls import path
from . import views
from .views import *


app_name="dashboard"
urlpatterns = [
    path('', views.index, name='index'),

    # path('signin/', views.signin, name='signin'),

    path('add/about',views.add_edit_About, name='add_About'),

    path('add/personalDetails',views.PersonalDetails, name='add_PersonalDetails'),

    path('add/service',views.add_edit_Service, name='add_Service'),
    path('edit/service/<int:id>/',views.add_edit_Service, name='edit_Service'),
    path('service/', ServiceListView.as_view(), name='Service'),
    path('service-delete/<int:id>/', ServiceDeleteView.as_view(), name='deleteService'),

    path('add/testimonial',views.add_edit_Testimonial, name='add_Testimonial'),
    path('edit/testimonial/<int:id>/',views.add_edit_Testimonial, name='edit_Testimonial'),
    path('testimonial/', TestimonialListView.as_view(), name='Testimonial'),
    path('testimonial-delete/<int:id>/', TestimonialDeleteView.as_view(), name='deleteTestimonial'),

    path('edit/contact/<int:id>/',views.add_edit_Contact, name='edit_Contact'),
    path('contact/', ContactListView.as_view(), name='Contact'),
    path('contact-delete/<int:id>/', ContactDeleteView.as_view(), name='deleteContact'),

    path('edit/appointment/<int:id>/',views.add_edit_Appointment, name='edit_Appointment'),
    path('appointment/', AppointmentListView.as_view(), name='Appointment'),
    path('appointment-delete/<int:id>/', AppointmentDeleteView.as_view(), name='deleteAppointment'),

    path('add/album',views.create_or_edit_album, name='add_Album'),
    path('editalbum/<int:album_id>/',views.create_or_edit_album, name='edit_Album'),
    path('album/', AlbumListView.as_view(), name='Album'),
    path('album-delete/<int:id>/', AlbumDeleteView.as_view(), name='deleteAlbum'),

    path('add/companydescription',views.add_edit_CompanyDescription, name='add_CompanyDescription'),
    path('edit/companydescription/<int:id>/',views.add_edit_CompanyDescription, name='edit_CompanyDescription'),
    path('companydescription/', CompanyDescriptionListView.as_view(), name='CompanyDescription'),
    path('companydescription-delete/<int:id>/', CompanyDescriptionDeleteView.as_view(), name='deleteCompanyDescription'),

    path('add/herobanner',views.HeroBanners, name='add_HeroBanner'),
]
