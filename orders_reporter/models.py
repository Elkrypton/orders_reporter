from django.db import models
import pyqrcode
# Create your models here.
from django.db import models

class Manufacturer(models.Model):
<<<<<<< HEAD
    parts = models.CharField(max_length=50)
    order_number = models.CharField(max_length=50)
    order_date = models.DateTimeField()
    sku = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=50)

=======
    vendor = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    store_sku = models.CharField(max_length=50)
    omsid = models.CharField(max_length=50)
    store_so_sku = models.CharField(max_length=50)
    parts_usage = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=50)


class SubmittedReport(models.Model):
    parts = models.CharField(max_length=100)
    order_date = models.DateField(max_length=100)
    order_number = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now=True)
>>>>>>> 5aba71bbc6b139b60dcc33661d0611782daf2da2
