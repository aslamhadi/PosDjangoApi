from django.db import models


class StoreInformation(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name
