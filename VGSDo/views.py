from django.shortcuts import render
from .models import Picture, Category, Event, Video
from django.db.models.query import QuerySet
from django import template
from django.template import loader
from django.http import HttpResponse
from django.db.models import Q


# Create your views here.
def index(request):
    date = Event.objects.all()
    events = Event.objects.all()
    context = {'events': events, 'date' : date}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')


def courses(request):
    return render(request, 'courses.html') 


def video(request):
    categories = Category.objects.all()
    title = Video.objects.all()
    thumb = Video.objects.all()
    context = {'categories': categories, 'title': title,
               'thumb' : thumb}
    return render(request, 'video.html', context)


def viddetails(request, pk):
    items = Video.objects.get(id=pk)
    context = {'items':items}
    return render(request, 'videodetail.html', context )



def viewphoto(request,pk):
    video = Video.objects.get(id=pk)
    return render(request, 'videodetail.html', {'video':video})

def photo(request):
    categories = Category.objects.all()
    pictures = Picture.objects.all()
    desc = Picture.objects.all()
    title = Picture.objects.all()
    context = {'categories': categories,
               'pictures': pictures, 'desc': desc, 'title': title}
    return render(request, 'photo.html', context)

def content(request):
    return render(request, 'content.html')



def search(request):

    results = []

    if request.method == "GET":

        query = request.GET.get('search')

        if query == "":

            query = 'None'

        results = Picture.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query) )
        context = {'query': query, 'results': results}

    return render(request, 'search.html', context)

def search2(request):

    results = []

    if request.method == "GET":

        query = request.GET.get('search')

        if query == "":

            query = 'None'

        results = Video.objects.filter(Q(title__icontains=query) | Q(desc__icontains=query) )
        context = {'query': query, 'results': results}

    return render(request, 'search2.html', context)


