from django.db import models

# Create your models here.

# create categories model
class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

#create Image Model
class Image(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='images')
    added_date=models.DateTimeField()
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)
    ram=models.TextField(default="")
    storage=models.TextField(default="")
    OperatingSystem=models.TextField(default="")
    Processor=models.TextField(default="")
    Price=models.TextField(default="")



    def __str__(self):
        return self.title
