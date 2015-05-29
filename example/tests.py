from hypothesis.extra.django import TestCase
from hypothesis.extra.django.models import models
from hypothesis import given
from hypothesis.strategies import integers, lists
from mysite.example.models import StockSubscription, Portfolio

class StockSubscriptionTestCase(TestCase):
    @given(models(StockSubscription))
    def test_next_notification_after_last_notification(self, subscription):
        self.assertTrue(subscription.next_notification_time > subscription.lastNotified)

class PortfolioTestCase(TestCase):
    @given(models(Portfolio), lists(models(StockSubscription, value=integers(min_value=1, max_value=100))))
    def test_median(self, portfolio, subs):
        portfolio.subscriptions.add(*subs)
        self.assertTrue(0 <= portfolio.median_value() < 101)
