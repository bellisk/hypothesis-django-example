from django.db import models
import datetime


class StockSubscription(models.Model):
    symbol = models.CharField(max_length=8)
    lastNotified = models.DateTimeField(auto_now_add=True)
    notificationsPerDay = models.IntegerField()
    value = models.IntegerField()

    def __str__(self):
        return '"{0}" {1} per day'.format(self.symbol, self.notificationsPerDay)

    @property
    def next_notification_time(self):
        return self.lastNotified + datetime.timedelta(hours=24/self.notificationsPerDay)


class Portfolio(models.Model):
    subscriptions = models.ManyToManyField(StockSubscription, related_name="portfolios")
    
    def median_value(self):
        return median([sub.value for sub in self.subscriptions.all()])
    
    def __str__(self):
        return "A portfolio of stock subscriptions."


def median(l):
    if len(l) == 0:
        return 0
    l = sorted(l)
    if len(l) % 2 == 0:
        return (l[len(l) / 2] + l[len(l) / 2 + 1]) / 2
    else:
        return l[len(l) / 2]
