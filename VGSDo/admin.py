from django.contrib import admin
from django.shortcuts import render
from .models import Category, Picture,Video,Event


# Register your models here.
admin.site.register(Category)
admin.site.register(Picture)
admin.site.register(Video)
admin.site.register(Event)

