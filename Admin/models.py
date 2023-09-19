from django.db import models

class Districts(models.Model):

    districtname = models.CharField(max_length=50, null=True)

    def __str__(self):

        return self.districtname

class Turflocation(models.Model):

    turflocation = models.ForeignKey(Districts, on_delete= models.CASCADE)

    tname = models.CharField(max_length=50, null=True)

    turfaddress = models.CharField(max_length=50)

    turfimage = models.ImageField(upload_to='data', default='null.jpg')

    placeprice = models.CharField(max_length=50, null=True) 

    
    def __str__(self):

        return self.turfaddress
    

class Extraimages(models.Model):

    location = models.ForeignKey(Turflocation, on_delete= models.CASCADE)

    additionalimages = models.ImageField(upload_to= 'data', default='null.jpg')


class Turfcategory(models.Model):

    category = models.CharField(max_length=50, null=True)

    categoryprice = models.CharField(max_length=50, null=True)
