from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.manage import PeriodManager
from eventex.core.models import Speaker, Contact, Talk


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(name='Thiago', slug='thiago',
                                              photo='http://hbn.link/hb-pic')

    def test_contact_email(self):
        """Speaker must have a contact"""
        Contact.objects.create(speaker=self.speaker, kind=Contact.EMAIL, value='email.net@gmail.com')

        self.assertTrue(Contact.objects.exists())

    def test_contact_phone(self):
        Contact.objects.create(speaker=self.speaker, kind=Contact.PHONE, value='11 0000-0000')
        self.assertTrue(Contact.objects.exists())

    def test_contact_choices(self):
        """Contact kind should be limited to E or P """
        contact = Contact(self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker, kind=Contact.EMAIL, value='email.net@gmail.com')
        self.assertEquals('email.net@gmail.com', str(contact))


class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
                name='Thiago',
                slug='thiago',
                photo='http://hb.link/hb-pic'
        )

        s.contact_set.create(kind=Contact.EMAIL, value='email.net@gmail.com')
        s.contact_set.create(kind=Contact.PHONE, value='11-00000000')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['email.net@gmail.com']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['11-00000000']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)


class PeriodManagerTest(TestCase):

    def setUp(self):
        Talk.objects.create(title='Talk at Morning', start='11:59')
        Talk.objects.create(title='Talk at afternoon', start='12:00')

    def test_period_manager(self):
        self.assertIsInstance(Talk.objects, PeriodManager)

    def test_at_morning(self):
        qs = Talk.objects.at_morning()
        expected = ['Talk at Morning']
        self.assertQuerysetEqual(qs, expected, lambda o: o.title)


    def test_at_afternoon(self):
        qs = Talk.objects.at_afternoon()
        expected = ['Talk at afternoon']
        self.assertQuerysetEqual(qs, expected, lambda o: o.title)
