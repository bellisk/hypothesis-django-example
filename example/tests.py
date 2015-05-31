from hypothesis.extra.django import TestCase
from hypothesis.extra.django.models import models
from hypothesis import given
from hypothesis.strategies import integers
from mysite.example.models import StockSubscription


class StockSubscriptionTestCase(TestCase):
    @given(models(StockSubscription, notificationsPerDay=integers()))
    def test_next_notification_after_last_notification(self, subscription):
        self.assertTrue(subscription.next_notification_time > subscription.lastNotified)