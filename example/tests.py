from hypothesis.extra.django import TestCase
from hypothesis.extra.django.models import models
from hypothesis import given
from hypothesis.strategies import integers
from mysite.example.models import StockSubscription, RelatedSubscription


class StockSubscriptionTestCase(TestCase):
    @given(models(StockSubscription))
    def test_next_notification_after_last_notification(self, subscription):
        self.assertTrue(subscription.next_notification_time > subscription.lastNotified)


class RelatedSubscriptionTestCase(TestCase):
    @given(models(RelatedSubscription, baseSubscription=models(StockSubscription)))
    def test_next_notification_same_as_base_subscription(self, related_subscription):
        self.assertEquals(
            related_subscription.next_notification_time,
            related_subscription.baseSubscription.next_notification_time
        )