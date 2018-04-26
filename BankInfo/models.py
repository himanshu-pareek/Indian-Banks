from django.db import models

# Create your models here.
class Bank (models.Model):
    id = models.BigIntegerField (null = False, default = 0, primary_key = True)
    name = models.CharField (max_length = 50, null = True)

class Branch (models.Model):
    ifsc = models.CharField (max_length = 11, primary_key = True)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE)
    branch = models.CharField (max_length = 74, null = True)
    address = models.CharField (max_length = 195, null = True)
    city = models.CharField (max_length = 50, null = True)
    district = models.CharField (max_length = 50, null = True)
    state = models.CharField (max_length = 26, null = True)
