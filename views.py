from django.template import RequestContext, loader
from django.http import HttpResponse
from djangit import settings

def index(request):
    t = loader.get_template('index.html')
    c = RequestContext(request, {
        'STATIC_URL':settings.STATIC_URL,
    } )
    return HttpResponse(t.render(c))

