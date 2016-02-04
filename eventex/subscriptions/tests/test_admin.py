from unittest.mock import Mock

from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionsModelAdmin, Subscription, admin


class SubscriptionModelAdmin(TestCase):
    def setUp(self):
        Subscription.objects.create(name="Thiago Olivieira", cpf=12345678901,
                                    email="oliveiravicente.net@gmail.com",
                                    phone="11-970513508")
        self.model_admin = SubscriptionsModelAdmin(Subscription, admin.site)
        self.queryset = Subscription.objects.all()

    def test_has_action(self):
        """ Action mark_as_paid should be installed """
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_as_paid(self):
        """it Should be all mark subscription as paid"""
        self.call_action()

        self.model_admin.mark_as_paid(None, self.queryset)
        self.assertEquals(1, Subscription.objects.filter(paid=True).count())

    def test_message(self):
        """it Should send message to user"""

        mock = self.call_action()
        self.model_admin.mark_as_paid(None, self.queryset)
        mock.assert_called_once_with(None, '1 inscrição foi marcada como paga.')

    def call_action(self):
        mock = Mock()
        old_message_user = self.model_admin.message_user
        SubscriptionsModelAdmin.message_user = mock

        Subscription.message_user = old_message_user
        return mock
