from django.test import TestCase
from eventex.core.models import Talk, Speaker, Curse
from django.shortcuts import resolve_url as r


class TalkListGet(TestCase):
    def setUp(self):
        talk1 = Talk.objects.create(title='Title talk about.', start='10:00',
                                    description='Description of talk about.')
        talk2 = Talk.objects.create(title='Title talk about.', start='13:00',
                                    description='Description of talk about.')
        c1 = Curse.objects.create(title='Titulo do curso', start='09:00',
                                  description='Descrição do curso', slot=20)

        speaker = Speaker.objects.create(name='Thiago Oliveira', slug='thiago-oliveira',
                                         website='http://hbn.link/hb.-site')

        talk1.speakers.add(speaker)
        talk2.speakers.add(speaker)
        c1.speakers.add(speaker)

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
            ('3', '/speakers/thiago-oliveira/'),
            ('3', 'Thiago Oliveira'),
            ('1', 'Titulo do curso'),
            ('1', 'Descrição do curso'),
            ('1', '09:00')
        ]

        for count, expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected, int(count))

    def test_context(self):
        variable = ['morning', 'afternoon', 'curses']
        for key in variable:
            with self.subTest():
                self.assertIn(key, self.resp.context)


class TalklistGetEmpty(TestCase):
    def test_get(self):
        """If is not talk in morning"""
        reponse = self.client.get(r('talk_list'))
        self.assertContains(reponse, 'Ainda não há pelastras marcadas para manhã.')
        self.assertContains(reponse, 'Ainda não há pelastras marcadas para tarde.')
