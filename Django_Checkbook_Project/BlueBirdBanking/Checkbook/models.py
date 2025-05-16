from django.db import models

# Create your models here.
class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    initial_deposit = models.DecimalField(decimal_places=2, max_digits=15)

    #define model manager for Accounts
    Accounts = models.Manager()

    #allow references to a specific account to be returned as the owner's name not the primary key
    def __str__(self):
        return self.first_name + ' ' + self.last_name


# Choices for a transaction:
TransactionTypes = [('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')]

class Transaction(models.Model):
    date = models.DateField()
    type = models.CharField(choices=TransactionTypes, max_length=10)
    amount = models.DecimalField(decimal_places=2, max_digits=15)
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    # define the model manager for Transactions
    Transactions = models.Manager()


