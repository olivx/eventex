from django.test import TestCase
from eventex.core.models import Talk, Speaker
from django.shortcuts import resolve_url as r


class TalkListGet(TestCase):
    def setUp(self):
        talk1 = Talk.objects.create(title='Title talk about.', start='10:00',
                                    description='Description of talk about.')
        talk2 = Talk.objects.create(title='Title talk about.', start='13:00',
                                    description='Description of talk about.')

        speaker = Speaker.objects.create(name='Thiago Oliveira', slug='thiago-oliveira',
                                         website='http://hbn.link/hb.-site')

        talk1.speakers.add(speaker)
        talk2.speakers.add(speaker)

        self.resp = self.client.get(r('talk_list'))

    def test_get(self):
        self.assertEquals(200, self.resp.status_code)

    def test_tempalet(self):
        """Should have used talk_list.html template"""
        self.assertTemplateUsed(self.resp, 'core/talk_list.html')

    def test_html(self):
        contents = [
            ('2', 'Title talk about.'),
            ('1', 'Manhã'),
            ('1', 'Tarde'),
            ('1', '10:00'),
            ('1', '13:00'),
            ('2', 'Description of talk about.'),
            ('2', '/speakers/thiago-oliveira/'),
            ('2', 'thiago-oliveira'),
        ]

        for count, expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected, int(count))

    def test_context(self):
        variable = ['morning', 'afternoon']
        for key in variable:
            with self.subTest():
                self.assertIn(key, self.resp.context)


class TalklistGetEmpty(TestCase):

    def test_get(self):
        """If is not talk in morning"""
        reponse = self.client.get(r('talk_list'))
        self.assertContains(reponse, 'Ainda não há pelastras marcadas para manhã.')
        self.assertContains(reponse, 'Ainda não há pelastras marcadas para tarde.')
