from django.db import models

# Create your models here.# -*- coding: utf-8 -*-
class userinfo(models.Model):
    name = models.CharField(max_length=30)
    pwd = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name






