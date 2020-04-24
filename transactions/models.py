from django.db import models
from categories.models import Category
from accounts.models import Account
class Transaction(models.Model):
    store = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    amount = models.FloatField()
    trans_date = models.DateField()
   #add a category as a foreign key later that pulls this in as a dropdown
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    account_name = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    def __str__(self):
        return '%s  %s  %s %s %s %s' %(self.store, self.description, self.amount, self.trans_date, self.category, self.account_name)