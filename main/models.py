from django.db import models

# Create your models here.


class Respondents(models.Model):
    subject = models.CharField(max_length=250)
    year_level = models.CharField(max_length=100)