from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def mindex(request):
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': 'iiiii',
    }
    return HttpResponse(template.render(context, request))