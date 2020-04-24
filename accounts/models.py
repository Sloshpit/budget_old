from django.db import models
class Account(models.Model):
    account_name = models.CharField(max_length=200)
    balance = models.FloatField()
    balance_date = models.DateField()
    def __str__(self):
         return '%s %s %s' % (self.account_name, self.balance, self.balance_date)
