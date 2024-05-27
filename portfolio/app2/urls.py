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
    path('Service/', ServiceListView.as_view(), name='Service'),
    path('Service-delete/<int:id>/', ServiceDeleteView.as_view(), name='deleteService'),

    path('add/testimonial',views.add_edit_Testimonial, name='add_Testimonial'),
    path('edit/testimonial/<int:id>/',views.add_edit_Testimonial, name='edit_Testimonial'),
    path('Testimonial/', TestimonialListView.as_view(), name='Testimonial'),
    path('Testimonial-delete/<int:id>/', TestimonialDeleteView.as_view(), name='deleteTestimonial'),

    path('edit/contact/<int:id>/',views.add_edit_Contact, name='edit_Contact'),
    path('Contact/', ContactListView.as_view(), name='Contact'),
    path('Contact-delete/<int:id>/', ContactDeleteView.as_view(), name='deleteContact'),

    path('edit/appointment/<int:id>/',views.add_edit_Appointment, name='edit_Appointment'),
    path('Appointment/', AppointmentListView.as_view(), name='Appointment'),
    path('Appointment-delete/<int:id>/', AppointmentDeleteView.as_view(), name='deleteAppointment'),

    path('add/album',views.create_or_edit_album, name='add_Album'),
    path('editalbum/<int:album_id>/',views.create_or_edit_album, name='edit_Album'),
    path('Album/', AlbumListView.as_view(), name='Album'),
    path('Album-delete/<int:id>/', AlbumDeleteView.as_view(), name='deleteAlbum'),

    path('add/companyDescription',views.add_edit_CompanyDescription, name='add_CompanyDescription'),
    path('edit/companyDescription/<int:id>/',views.add_edit_CompanyDescription, name='edit_CompanyDescription'),
    path('CompanyDescription/', CompanyDescriptionListView.as_view(), name='CompanyDescription'),
    path('CompanyDescription-delete/<int:id>/', CompanyDescriptionDeleteView.as_view(), name='deleteCompanyDescription'),

    path('add/herobanner',views.HeroBanners, name='add_HeroBanner'),
]
