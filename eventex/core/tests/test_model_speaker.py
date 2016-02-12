from django.test import TestCase
from eventex.core.models import Speaker
from django.shortcuts import resolve_url as r


class SpeakerModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
                name='Grace Hopper', slug='grace-hopper',
                photo='http://hbn.link/hopper-pic',
                website='http://hbn.link/hopper-site',
                description='Programadora e almirante.'
        )

    def test_model(self):
        """Model speaker should have in context name,slug,photo,website,description"""
        self.assertTrue(Speaker.objects.exists())

    def test_description_can_be_blank(self):
        """Description can be blank"""
        field = Speaker._meta.get_field('description')
        self.assertTrue(field.blank)

    def test_website_can_be_blank(self):
        """"Website can be blank"""
        field = Speaker._meta.get_field('website')
        self.assertTrue(field.blank)

    def test_str(self):
        self.assertEquals('Grace Hopper', str(self.speaker))

    def test_get_absolute_url(self):
        url = r('speaker_detail', slug=self.speaker.slug)
        self.assertEquals(url, self.speaker.get_absolute_url())
