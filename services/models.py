from django.db import models

class ServiceCatagory(models.Model):
    catagory_name = models.CharField(max_length=200)
    def __str__(self):
        return self.catagory_name

class ServiceAdd(models.Model):
    service_name = models.CharField(max_length=200)
    catagory = models.ForeignKey(ServiceCatagory)
    provider = models.CharField(max_length=200, unique=True)
    photo = models.ImageField(upload_to='service_image', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField()
    def __str__(self):
        return self.service_name
# Create your models here.
