from django.http import HttpResponse
from django.template import loader
from .models import Image


def gallery(request):
    gallery_images = Image.objects.all()
    template = loader.get_template('gallery/gallery.html')
    context = {
        'gallery_images' : gallery_images
    }
    return HttpResponse(template.render(context, request))
# Create your views here.
