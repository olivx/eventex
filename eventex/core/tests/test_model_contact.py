from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact


class ContactModel(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(name='Thiago Oliveira', slug='thiago-oliveira',
                                              photo='http://hbn.link/hb-pic')

    def test_contact_email(self):
        """Speaker must have a contact"""
        Contact.objects.create(speaker=self.speaker, kind=Contact.EMAIL, value='oliveiravicente.net@gmail.com')

        self.assertTrue(Contact.objects.exists())

    def test_contact_phone(self):
        Contact.objects.create(speaker=self.speaker, kind=Contact.PHONE, value='11 97051-3508')
        self.assertTrue(Contact.objects.exists())

    def test_contact_choices(self):
        """Contact kind should be limited to E or P """
        contact = Contact(self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker, kind=Contact.EMAIL, value='oliveiravicente.net@gmail.com')
        self.assertEquals('oliveiravicente.net@gmail.com', str(contact))