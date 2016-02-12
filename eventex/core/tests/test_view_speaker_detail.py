from django.test import TestCase
from django.shortcuts import resolve_url as r
from eventex.core.models import Speaker


class SpeakerDetailGet(TestCase):
    def setUp(self):
        Speaker.objects.create(
                name='Grace Hopper',
                slug='grace-hopper',
                photo='http://hbn.link/hopper-pic',
                website='http://hbn.link/hopper-site',
                description='Programadora e almirante.'
        )
        self.resp = self.client.get(r('speaker_detail', slug='grace-hopper'))

    def test_get(self):
        """should have return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """should be used template speaker_detail.html"""
        self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')

    def test_html(self):
        expected = [
            'Grace Hopper',
            'http://hbn.link/hopper-site',
            'http://hbn.link/hopper-pic',
            'Programadora e almirante.'
        ]

        for ex in expected:
            with self.subTest():
                self.assertContains(self.resp, ex)

    def test_contex_speaker(self):
        """Should have instace the speaker"""
        speaker = self.resp.context['speaker']
        self.assertIsInstance(speaker, Speaker)


class SpeakerIsNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get(r('speaker_detail', slug='not-found'))
        self.assertEquals(404, response.status_code)


