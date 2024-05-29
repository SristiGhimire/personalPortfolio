from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.fields.files import ImageField 

class PersonalDetail(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    logo = models.FileField(upload_to="logo")
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    facebookUrl = models.URLField()
    twiterUrl = models.URLField()
    instagramUrl = models.URLField()
    whatsappUrl = models.URLField()
    description = RichTextField()
    companyName = models.CharField(max_length=200)
    image = models.FileField(upload_to="smallImage")
    favicon = models.FileField(upload_to="Favicon")
    mapUrl = models.URLField()


    def __str__(self):
        return self.firstName

    class Meta:
        ordering = ['-id']

class Service(models.Model):
    logo = models.FileField(upload_to="serviceimage")
    title = models.CharField(max_length=25)
    description=RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

class Album(models.Model):
    title = models.CharField(max_length=50)
    image = models.FileField(upload_to="albumimage/")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

class Gallery(models.Model):
    gallery = models.ForeignKey(Album, on_delete= models.SET_NULL,null=True, blank=True,  related_name ='albums')
    image = models.FileField(upload_to="galleryimage")
    class Meta:
        ordering = ['-id']
class Contact(models.Model):
    name = models.CharField(max_length=50)
    contact = models.IntegerField()
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

class About(models.Model):
    image=models.FileField(upload_to="aboutimage")
    title=models.CharField(max_length=200)
    subtitle=models.CharField(max_length=200)
    subdescription = models.CharField(max_length=400)
    description=RichTextField()
    completedProject = models.CharField(max_length=400)
    satisfiedClient = models.CharField(max_length=400)

    def __str__(self):
        return self.title

class Appointment(models.Model):
    name=models.CharField(max_length=50)
    phone = models.IntegerField()
    startdate=models.DateTimeField()

    def __str__(self):
        return self.name

class Client(models.Model):
    title = models.CharField(max_length=200)
    time = models.CharField(max_length= 200)
    name = models.CharField(max_length=200)
    icon = models.FileField(upload_to="clientIconimage")
    description = RichTextField()

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="testimonialimage")
    description = RichTextField(null=False, blank=False)

    def __str__(self):
        return self.name

class CompanyDescription(models.Model):
    time = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    icon = models.ImageField(upload_to="companydescriptionimage")
    description = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

class Herobanner(models.Model):
    image = models.ImageField(upload_to="herobannerimage")
    subDescription = models.CharField(max_length=400)
    description = RichTextField()
    
    def __str__(self):
        return self.subDescription
        








