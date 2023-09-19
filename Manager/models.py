from django.db import models
from Admin.models import *

class Managerregister(models.Model):

    managerfname = models.CharField(max_length=50)

    managerlname = models.CharField(max_length=50)

    manageraddress = models.CharField(max_length=50)

    managercities = models.CharField(max_length=50)

    managerphone = models.CharField(max_length=50)

    manageremail = models.CharField(max_length=50)

    managerpassword = models.CharField(max_length=50)

    assignedturf = models.ForeignKey(Turflocation,on_delete=models.CASCADE, null=True)

    designation = models.CharField(max_length=50, default="manager")

    managerstatus = models.CharField(max_length=50, default=0)
    