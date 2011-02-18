from django.template import RequestContext, loader
from django.http import HttpResponse
from djangit import settings
from djangit.release.models import Branch

from subprocess import Popen, PIPE

def index(request):
    t = loader.get_template('index.html')
    c = RequestContext(request, {
        'STATIC_URL':settings.STATIC_URL,
    } )
    return HttpResponse(t.render(c))

def beta(request, beta_id = None):
    betas = Branch.objects.filter(type='B')
    t = loader.get_template('beta.html')
    context_dict = {
        'STATIC_URL':settings.STATIC_URL,
        'betas':betas
    }
    if beta_id != None:
        beta = Branch.objects.filter(id=beta_id)[0]
        output = Popen(\
            ['ssh', beta.server.user + '@' + str(beta.server),
            'cd ' + beta.repo.repo + '; ' + \
            'git checkout ' + beta.target + '; ' + \
            'git merge ' + beta.source + '; ' + \
            'cd ' + beta.path + '; ' + \
            'git checkout ' + beta.target + '; ' + \
            'git pull'], stdout=PIPE, stderr=PIPE).communicate()
        output = ''.join([result for result in output])
        context_dict['output'] = output
        context_dict['branch'] = beta
    c = RequestContext(request, context_dict)
    return HttpResponse(t.render(c))

def release(request, release_id = None):
    releases = Branch.objects.filter(type='R')
    t = loader.get_template('release.html')
    context_dict = {
        'STATIC_URL':settings.STATIC_URL,
        'releases':releases
    }
    if release_id != None:
        release = Branch.objects.filter(id=release_id)[0]
        output = Popen(\
            ['ssh', release.server.user + '@' + str(release.server),
            'cd ' + release.repo.repo + '; ' + \
            'git checkout ' + release.target + '; ' + \
            'git merge ' + release.source + '; ' + \
            'cd ' + release.path + '; ' + \
            'git checkout ' + release.target + '; ' + \
            'git pull'], stdout=PIPE, stderr=PIPE).communicate()
        output = ''.join([result for result in output])
        context_dict['output'] = output
        context_dict['branch'] = release
    c = RequestContext(request, context_dict)
    return HttpResponse(t.render(c))
