from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model, CharField, ForeignKey, CASCADE, DecimalField, DateField
from django.db.models.enums import TextChoices
from django.contrib.auth.models import AbstractUser

class Category(Model):
    class CategoryType(TextChoices):
        INCOME = 'income', 'Income'
        EXPENSES = 'expenses', 'Expenses'
    name = CharField(max_length=255)
    type = CharField(max_length=10, choices=CategoryType.choices)

    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name


class Wallet(Model):
    INCOME = 'income'
    EXPENSES = 'expenses'

    class WalletChoices(TextChoices):
        INCOME = 'income', 'Income'
        EXPENSES = 'expenses', 'Expenses'

    user = ForeignKey(User, on_delete=CASCADE)
    category = ForeignKey(Category, on_delete=CASCADE)
    amount = DecimalField(max_digits=10, decimal_places=2)
    status = CharField(max_length=10, choices=WalletChoices.choices)
    date = DateField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    @staticmethod
    def user_balance(user):
        income = Wallet.objects.filter(user=user, status='income').aggregate(models.Sum('amount'))['amount__sum']
        expenses = Wallet.objects.filter(user=user, status='expense').aggregate(models.Sum('amount'))[ 'amount__sum']
        wallet = Wallet.objects.filter(user=user)
        if not expenses:
            expenses = 0
        if not income:
            income = 0
        return {"balance": income - expenses , "income": income , "expenses": expenses , "wallets": wallet}










