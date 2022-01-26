from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    query= models.TextField()
    date =  models.DateField()

    def __str__(self):
        return self.name
class Donate(models.Model):
    name= models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    money=models.CharField(max_length=100)
    payment= models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
    date = models.DateField()

    def __str__(self):
        return self.name
