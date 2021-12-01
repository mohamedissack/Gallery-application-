from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=50)

    def save_location(self):
        self.save()
    def delete_location(self):
        self.delete()

    @classmethod
    def get_locations(cls):
        return Location.objects.all()

    @classmethod
    def update_location(cls,id,value):
        cls.objects.filter(id=id).update(name=value)

    def __str__(self):
        return self.name

class Catergory(models.Model):
    name= models.CharField(max_length=50 )

    def save_catergory(self):
        self.save()
    
    def delete_catergory(self):
        self.delete()

    @classmethod
    def get_catergory(cls):
        return Catergory.objects.all() 

    def __str__(self):
        return self.name           

class Image(models.Model):
    name = models.CharField(max_length = 60)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    image = CloudinaryField('image',blank=True,null=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    catergory = models.ForeignKey(Catergory,on_delete=models.CASCADE)

    @classmethod
    def get_image_by_id(cls,id):
        image = Image.objects.filter(id=id).all()
        return image

    @classmethod
    def update_image(cls,id,value):
        cls.objects.filter(pk=id).update(image=value)

    @classmethod
    def filter_by_location(cls,location):
        img_location = Image.objects.filter(location__name=location).all()
        return img_location

    @classmethod
    def filter_by_catergory(cls,catergory):
        img_catergory = Image.objects.filter(catergory__name=catergory).all()
        return img_catergory
    

    @classmethod
    def search_by_catergory(cls,catergory):
        image = cls.objects.filter(catergory__name__icontains=catergory)
        return image

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def __str__(self):
        return self.name


