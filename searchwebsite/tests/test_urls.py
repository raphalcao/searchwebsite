from django.test import SimpleTestCase
from django.urls import reverse, resolve
from searchwebsite.views import localhost, search, sites_view


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('list')
        self.assertEquals(resolve(url).func, localhost)

    def test_list_url_search(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, search)

    def test_list_url_json(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func, sites_view)



