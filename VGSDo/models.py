from django.db import models
from django.db.models.fields import DateField
from django.conf import settings
from hashid_field import HashidAutoField
# from multiselectfield import MultiSelectField
from embed_video.fields import EmbedVideoField



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)


    def __str__(self):
        return self.name



class Picture(models.Model):
    id = HashidAutoField(primary_key=True, min_length=9)
    name = models.TextField(max_length=50, null=False)
    added = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(null=False, blank=False)
    desc = models.TextField(max_length=200, null=False)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['added']


class Video(models.Model):
    id = HashidAutoField(primary_key=True, min_length=9)
    title = models.TextField(max_length=100, null=False, blank=False)
    desc = models.TextField(max_length=100, null= False, blank= False)
    added = models.DateTimeField(auto_now_add=True)
    video = EmbedVideoField() 
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
        
    
    class Meta:
        ordering = ['added']


class Event(models.Model):
    id = HashidAutoField(primary_key=True, min_length=9)
    poster = models.ImageField(null=False, blank=False)
    name = models.TextField(max_length=100, null=False, blank=False)
    date = models.DateTimeField(null=True)
    place = models.TextField(max_length=100, null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['added']
    

