from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.

def index(request):
    template = loader.get_template('app/index.html')
    context = RequestContext(request, {
        'sentence' : 'My name is ryan'
    })
    return HttpResponse(template.render(context))
