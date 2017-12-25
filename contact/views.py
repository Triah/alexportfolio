from django.http import HttpResponse
from django.template import loader
#from .models import Image


def contact(request):
    #gallery_images = Image.objects.all()
    template = loader.get_template('contact/contact.html')
    #context = {
    #    'gallery_images' : gallery_images
    #}
    return HttpResponse(template.render(request))