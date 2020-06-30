from django.test import TestCase
from model_mommy import mommy

from searchwebsite.models import Website


class WebsiteTestCase(TestCase):
    def setUp(self):
        self.name = mommy.make('Website')

    def test_str(self):
        self.assertEquals(str(self.name), self.name.name)
