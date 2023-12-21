from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def setup(request):
    template = loader.get_template('index.html')
    context = {
        'id': "test",
    }
    return HttpResponse(template.render(context, request))