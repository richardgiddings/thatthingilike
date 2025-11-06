from django.shortcuts import render

from .models import Thing
from .forms import TagForm, LocationForm

def index(request):
    
    tag = request.GET.get('tag', None)
    location = request.GET.get('location', None)

    things = Thing.objects.filter(tag=tag, location=location)

    # get location dropdown
    locations = LocationForm(initial={'location': location})

    # get tag dropdown
    tags = TagForm(initial={'tag': tag})

    return render(request, 
                    template_name='thatthingilike/index.html',
                    context={'things': things, 
                             'locations': locations,
                             'tags': tags})
