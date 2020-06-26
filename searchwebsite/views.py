from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Website


def localhost(request):
    search = Website.objects.all()
    return render(request, 'index.html', {'searchs': search})


def search(request):
    nome = request.POST['text1']
    search = Website.objects.filter(name=nome)

    return render(request, 'index.html', {'search': search})


@api_view(['GET'])
def sites_view(request):
    website = Website.objects.all()
    output = [{
        'name': search.name,
        'link': search.link,
        'description': search.description
    } for search in website]

    return Response(output)
