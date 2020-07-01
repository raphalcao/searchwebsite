from django.test import TestCase, Client
from django.urls import reverse
from searchwebsite.models import Website
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list')
        self.sites_view = reverse('search')
        self.project1 = Website.objects.filter(
            name='globo'
        )

    def test_localhost_GET(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_sites_view(self):
        response = self.client.get(self.sites_view)
        self.assertEquals(response.status_code, 200)

    def test_search_POST(self):
        Website.objects.filter(
            name=self.project1
        )
        response = self.client.post(self.list_url, {

            "name": "globo",
            "link": "https://www.globo.com/",
            "description": "Só na globo.com você encontra tudo sobre o conteúdo e marcas do Grupo Globo. O melhor acervo de vídeos online sobre entretenimento, esportes e ..."
        })

        self.assertEquals(response.status_code, 200)
