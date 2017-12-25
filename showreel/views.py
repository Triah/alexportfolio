from django.http import HttpResponse
from django.template import loader
#from .models import Image


def showreel(request):
    template = loader.get_template('showreel/showreel.html')
    #context = {
     #   'gallery_images' : gallery_images
    #}
    return HttpResponse(template.render(request))