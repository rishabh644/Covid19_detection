from django.db import models
import os
# Create your models here.

def upload_path(instance,filename):
    return os.path.join("uploads",filename)
class Pdata(models.Model):
    name=models.CharField(max_length=200,null=False,default="krishna")
    dob=models.DateField(null=False,blank=True)
    def __str__(self):
        return self.name
class ImageModel(models.Model):
    image=models.ImageField(upload_to=upload_path,null=False,blank=True)
    created_date=models.DateTimeField(null=False,blank=True,auto_now_add=True)
    def fx(self):
        return self.image.name

