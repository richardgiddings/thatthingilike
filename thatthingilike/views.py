from django.shortcuts import render

from .models import Thing
from .forms import TagForm, LocationForm

from django.core.paginator import Paginator

def index(request):
    
    tag = request.GET.get('tag', None)
    location = request.GET.get('location', None)

    things = Thing.objects.filter(tag=tag, location=location).order_by('-date_added')
    paginator = Paginator(things, 2) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # get location dropdown
    locations = LocationForm(initial={'location': location})

    # get tag dropdown
    tags = TagForm(initial={'tag': tag})

    return render(request, 
                    template_name='thatthingilike/index.html',
                    context={
                        'locations': locations,
                        'tags': tags,
                        'selected_location': location,
                        'selected_tag': tag,                             
                        "page_obj": page_obj
                    })
