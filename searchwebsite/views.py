from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Website


def localhost(request):
    return render(request, 'index.html')


def search(request):
    nome = request.POST['text1'].lower()
    var_search = Website.objects.filter(name=nome)
    return render(request, 'index.html', {'search': var_search})


@api_view(['GET'])
def sites_view(request):
    website = Website.objects.all()
    output = [{
        'name': var_search.name,
        'link': var_search.link,
        'description': search.description
    } for var_search in website]
    return Response(output)
