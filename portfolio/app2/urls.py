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

    path('edit/contact/<int:id>/',views.add_edit_Contact, name='edit_Contact'),
    path('Contact/', ContactListView.as_view(), name='Contact'),
    path('Contact-delete/<int:id>/', ContactDeleteView.as_view(), name='deleteContact'),
]
