from django.db import models

# Create your models here.



class ContactMessage(models.Model):

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()    
    
    def __str__(self):
        return f"{self.name})"
    



class AboutModel(models.Model):
    objects = None
    image = models.ImageField(upload_to='images/about')
    text = models.TextField()
    

    def __str__(self):
        return f'({self.text})'


class ProductModel(models.Model):
    title = models.CharField(max_length = 30)
    text = models.TextField()
    image = models.ImageField(upload_to='images/product')
    describe = models.CharField(max_length=200)


    def __str__(self):
        return f"{(self.title)}-{(self.describe)}"


class ProductDescribe(models.Model):
    text = models.TextField()


class GalleryModel(models.Model):
    title = models.CharField(max_length=240)
    image = models.ImageField(upload_to='images/gallery')


    def __str__(self):
        return f'{(self.title)}' 
    
    