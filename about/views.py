from django.http import HttpResponse
from django.template import loader
#from .models import Image


def about(request):
    #gallery_images = Image.objects.all()
    template = loader.get_template('about/about.html')
    #context = {
    #    'gallery_images' : gallery_images
    #}
    return HttpResponse(template.render(request))