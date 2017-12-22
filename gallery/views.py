from django.shortcuts import render
from .models import Image


def gallery(request):
    gallery_images = Image.objects.all()
    context = {'gallery_images': gallery_images}
    return render(request, 'gallery.html', context)

# Create your views here.
