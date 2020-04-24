from django.db import models
class Account(models.Model):
    account_name = models.CharField(max_length=200)
    transaction = models.CharField(max_length=200)
    transaction_amount = models.FloatField()
    transaction_date = models.DateField()
    balance = models.FloatField()
    
    def __str__(self):
         return '%s %s %s %s %s' % (self.account_name, self.transaction, self.transaction_amount, self.transaction_date, self.balance)