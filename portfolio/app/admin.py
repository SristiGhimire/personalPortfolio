from django.contrib import admin
from .models import *

admin.site.register(PersonalDetail)
admin.site.register(About)
admin.site.register(Album)
admin.site.register(Gallery)
admin.site.register(Contact)
admin.site.register(Client)
admin.site.register(Testimonial)
admin.site.register(CompanyDescription)
admin.site.register(Herobanner)


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'startdate'] 

admin.site.register(Appointment, AppointmentAdmin)