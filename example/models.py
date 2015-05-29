from django.db import models
import datetime

# Create your models here.
class StockSubscription(models.Model):
    symbol = models.CharField(max_length=8)
    lastNotified = models.DateTimeField(auto_now_add=True)
    notificationsPerDay = models.IntegerField()

    def __str__(self):
        return '"' + self.symbol + '" ' + str(self.notificationsPerDay) + ' per day'

    @property
    def nextNotificationTime(self):
        return self.lastNotified + datetime.timedelta(hours=24/self.notificationsPerDay)