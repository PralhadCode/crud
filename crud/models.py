from django.db import models

class Record(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone = models.IntegerField()
    address =models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=200)
    country = models.CharField(max_length=100)

