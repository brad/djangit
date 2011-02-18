from django.template import RequestContext, loader
from django.http import HttpResponse
from djangit import settings
from djangit.release.models import Branch

def index(request):
    t = loader.get_template('index.html')
    c = RequestContext(request, {
        'STATIC_URL':settings.STATIC_URL,
    } )
    return HttpResponse(t.render(c))

def beta(request, beta_id = None):
    betas = Branch.objects.filter(type='B') 
    t = loader.get_template('beta.html')
    c = RequestContext(request, {
        'STATIC_URL':settings.STATIC_URL,
        'betas':betas
    } )
    return HttpResponse(t.render(c))

def release(request, release_id = None):
    releases = Branch.objects.filter(type='R')
    t = loader.get_template('release.html')
    c = RequestContext(request, {
        'STATIC_URL':settings.STATIC_URL,
	'releases':releases
    } )
    return HttpResponse(t.render(c))
