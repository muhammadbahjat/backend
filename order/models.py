from django.db import models

# Create your models here.
class OrderRecieved(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False)
    table_number = models.CharField(max_length=50,  null=False, blank=False)
    item_name = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name + " - Table " + self.table_number
