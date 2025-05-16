from django.forms import ModelForm
from .models import Account, Transaction


# create Account form for Account Model
class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'


# create Transaction form for Transaction Model
class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
