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
    description = models.TextField()


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
    image = models.FileField(upload_to="albumimage")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

class Gallery(models.Model):
    album = models.ForeignKey(Album, on_delete= models.SET_NULL,null=True, blank=True,  related_name ='hostings')
    image = models.FileField(upload_to="galleryimage")
    class Meta:
        ordering = ['-id']

class Contact(models.Model):
    name = models.CharField(max_length=50)
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
    description=RichTextField()

    def __str__(self):
        return self.title

class Appointment(models.Model):
    startdate=models.DateTimeField()

    def __str__(self):
        return self.startdate



