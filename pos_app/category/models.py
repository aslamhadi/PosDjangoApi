from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name