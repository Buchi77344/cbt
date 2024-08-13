from django.db import models

class Wallet(models.Model):
    address = models.CharField(max_length=100, unique=True)
    sol_balance = models.DecimalField(max_digits=20, decimal_places=8)
    profit = models.DecimalField(max_digits=20, decimal_places=8)
    win_rate = models.FloatField()
    total_trades = models.IntegerField()

class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    trade_type = models.CharField(max_length=10)  # 'buy' or 'sell'
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    price = models.DecimalField(max_digits=20, decimal_places=8)
    date = models.DateTimeField()


class Question(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
    

# models.py
from django.db import models
from django.contrib.auth.models import User

class UserID(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    generated_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.generated_id

