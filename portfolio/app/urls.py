from django.urls import path
from . import views

app_name="app"
urlpatterns = [
    path('',views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('appointment', views.appointment, name='appointment'),
    ]


