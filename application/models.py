from django.db import models

# Create your models here.


class contactinformation(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.fname