from django.test import TestCase
from eventex.core.manage import PeriodManager
from eventex.core.models import Talk, Curse


class TalkListGetTes(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(title='Title talk about.')

    def test_create_talk(self):
        self.assertTrue(Talk.objects.exists())

    def test_has_speaker(self):
        """Speaker should have a talk"""
        self.assertEquals(1, Talk.objects.count())

    def test_description_can_be_blank(self):
        """Description can be blank"""
        field = Talk._meta.get_field('description')
        self.assertTrue(field.blank)

    def test_start_can_be_blank(self):
        """Start can be blank"""
        field = Talk._meta.get_field('start')
        self.assertTrue(field.blank)

    def test_start_can_be_null(self):
        """Start can be null"""
        field = Talk._meta.get_field('start')
        self.assertTrue(field.null)

    def test_speaker_can_be_blank(self):
        """Speaker can be blank"""
        field = Talk._meta.get_field('speakers')
        self.assertTrue(field.blank)

class CorsesModelTest(TestCase):

    def setUp(self):
        self.curse = Curse.objects.create(title='Titulo do curso', start='09:00',
                              description='Descrição do curse', slot=20)

    def test_create(self):
        self.assertTrue(Curse.objects.exists())

    def test_speakers(self):
        """Curse has skpeaser and vice-versa"""
        self.curse.speakers.create(name='Thiago Oliveira', slug='thiago-oliveira',
                                   website='http://hb.link/hb-site')
        self.assertEqual(1, self.curse.speakers.count())

    def test_str(self):
        self.assertEqual('Titulo do curso', str(self.curse))

    def test_period_manager(self):
        self.assertIsInstance(Curse.objects, PeriodManager)