from django.db import models

# Create your models here.

class Shift(models.Model):
    id_shift = models.CharField(max_length=2)
    masuk = models.TimeField()
    pulang = models.TimeField()