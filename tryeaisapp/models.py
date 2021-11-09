from django.db import models
from django.db.models.fields import BooleanField, DateTimeField
from django.contrib.auth.models import User
# Create your models here.
# model for income, expense and loan records
class Accounts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    category = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=4)
    date = models.DateField()
    created_on = DateTimeField(auto_now_add=True)
    last_update = DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Account"

# used in the settings.html page
class Profile(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    budget = models.DecimalField(max_digits=10, decimal_places=4)
    photo = models.ImageField(upload_to='images')
    daily_reminder = models.BooleanField(default=False)
    weekly_reminder = models.BooleanField(default=False)
    monthly_reminder = models.BooleanField(default=False)
    yearly_reminder = models.BooleanField(default=False)
    daily_report = models.BooleanField(default=False)
    weekly_report = models.BooleanField(default=False)
    monthly_report = models.BooleanField(default=False)
    yearly_report = models.BooleanField(default=False)
    
